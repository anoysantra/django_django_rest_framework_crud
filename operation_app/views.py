from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cricketers, Batting_Record, Bowling_Record
from .serializers import  CricketerSerializer, BattingSerializer, BowlingSerializer 
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



#add cricketer bio along with batting and bowling record
@api_view(['POST'])
def add_cricketers(request):
  
    if request.method == 'POST':
        
        cricketer_data = request.data.get('cricketer')
        batting_record_data = request.data.get('batting')
        bowling_record_data = request.data.get('bowling')

        cricketer_serializer = CricketerSerializer(data=cricketer_data)
        batting_record_serializer = BattingSerializer(data=batting_record_data)
        bowling_record_serializer = BowlingSerializer(data=bowling_record_data)
        errors = {}

        if cricketer_serializer.is_valid():
            cricketer_serializer.save()
            cricketer_instance = cricketer_serializer.instance
            player_id = cricketer_instance.player_id
            
            #batting
            batting_record_serializer.initial_data['player'] = player_id
            if batting_record_serializer.is_valid():
                batting_record_serializer.save()
            else:
                errors['batting'] = [
                    {'field': field, 'message': msg}
                    for field, msg in batting_record_serializer.errors.items()
                ]
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)

            #bowling
            bowling_record_serializer.initial_data['player'] = player_id
            if bowling_record_serializer.is_valid():
                bowling_record_serializer.save()
            else:
                errors['bowling'] = [
                    {'field': field, 'message': msg}
                    for field, msg in bowling_record_serializer.errors.items()
                ]
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': 'Cricketer data saved successfully'})
        
        else:
            errors['cricketer'] = [
                {'field': field, 'message': msg}
                for field, msg in cricketer_serializer.errors.items()
            ]
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    

#get the all the cricketers bio along with the batting and bowling record
@api_view(['GET'])
def get_all_cricketers(request):

    if request.method == "GET":

        cricketers = Cricketers.objects.all()
        cricketer_batting_serializer = CricketerSerializer(cricketers, many =True)

        batting_record = Batting_Record.objects.all()
        batting_record_serializer = BattingSerializer(batting_record, many=True)

        bowling_record = Bowling_Record.objects.all()
        bowling_record_serializer = BowlingSerializer(bowling_record, many=True)

        response_data = [
            cricketer_batting_serializer.data,
            batting_record_serializer.data,
            bowling_record_serializer.data,
        ]
        return Response(response_data,status=status.HTTP_200_OK)


#get the batting bowling and profile data for a specific player.
@api_view(['GET'])
def get_specific_player(request,player_id):
    print(player_id)
   
    try:
        cricketer = Cricketers.objects.get(player_id=player_id)
    except Cricketers.DoesNotExist:
        return Response({'error':'Cricketer Not Found'},status=status.HTTP_404_NOT_FOUND)
    try:
        batting_record = Batting_Record.objects.get(player=player_id)
    except Batting_Record.DoesNotExist:
        return Response({'error': 'Batting Record Not Found'}, status=status.HTTP_404_NOT_FOUND)
    try:
        bowling_record = Bowling_Record.objects.get(player=player_id)
    except Bowling_Record.DoesNotExist:
        return Response({'error': 'Bowling Record Not Found'}, status=status.HTTP_404_NOT_FOUND)
  

    if request.method == 'GET':
        cricketer_serializer = CricketerSerializer(cricketer)
        batting_record_serializer = BattingSerializer(batting_record)
        bowling_record_serializer = BowlingSerializer(bowling_record)
        print('Found')
        response_data = [
            cricketer_serializer.data,
            batting_record_serializer.data,
            bowling_record_serializer.data
        ]
        return Response(response_data,status= status.HTTP_200_OK)



#to update or delete the main cricketer profile information
@api_view(['GET','POST','DELETE'])
def update_delete_cricketer(request,player_id):
    
    cricketer = get_object_or_404(Cricketers,player_id=player_id)
    if request.method == 'POST':
        cricketer_serializer = CricketerSerializer(instance=cricketer , data = request.data)
        if cricketer_serializer.is_valid():
            cricketer_serializer.save()
            return Response(cricketer_serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(cricketer_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        cricketer.delete()
        return Response("Cricketer Profile Deleted" , status = status.HTTP_204_NO_CONTENT)



#..........batting..........
#will show the batting stats of a specific player and update any batting specific stats. Deleteion not allowed
@api_view(['GET', 'POST'])
def manipulate_player_batting(request, player_id):
    cricketer_batting = get_object_or_404(Batting_Record, player=player_id)

    if request.method == 'GET':
        cricketer_batting_serializer = BattingSerializer(cricketer_batting)
        return Response(cricketer_batting_serializer.data)

    if request.method == 'POST':
        cricketer_batting_serializer = BattingSerializer(
            instance=cricketer_batting, data=request.data)
        if cricketer_batting_serializer.is_valid():
            cricketer_batting_serializer.save()
            return Response(cricketer_batting_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(cricketer_batting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


#.........bowling..............................
#Get the bowling stat of a specific player and update . Deletion now allowed
@api_view(['GET', 'POST'])
def manipulate_player_bowling(request, player_id):
    cricketer_bowling = get_object_or_404(Bowling_Record, player=player_id)

    if request.method == 'GET':
        cricketer_bowling_serializer = BowlingSerializer(cricketer_bowling)
        return Response(cricketer_bowling_serializer.data)

    if request.method == 'POST':
        cricketer_bowling_serializer = BowlingSerializer(
            instance=cricketer_bowling, data=request.data)
        if cricketer_bowling_serializer.is_valid():
            cricketer_bowling_serializer.save()
            return Response(cricketer_bowling_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(cricketer_bowling_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





        
    
        
    








    



