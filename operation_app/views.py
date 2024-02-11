from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cricketers, Batting_Record, Bowling_Record
from .serializers import  CricketerSerializer, BattingSerializer, BowlingSerializer 
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def add_cricketers(request):
    """
    if request.method == 'POST':
        print(request.data)
        cricketer_batting_data = request.data.get('cricketer')
        batting_record_data = request.data.get('batting')
        bowling_record_data = request.data.get('bowling')

        cricketer_batting_serializer = CricketerSerializer(data=cricketer_batting_data)
        batting_record_serializer = BattingSerializer(data=batting_record_data)
        bowling_record_serializer = BowlingSerializer(data=bowling_record_data)

        try:
            if cricketer_batting_serializer.is_valid() and batting_record_serializer.is_valid() and bowling_record_serializer.is_valid():
                cricketer_instance = cricketer_batting_serializer.save()
                batting_record_serializer.save(player=cricketer_instance)
                bowling_record_serializer.save(player=cricketer_instance)
                return Response("Data Saved Successfully", status=status.HTTP_201_CREATED)
            else:
                # Concatenate serializer errors
                raise serializers.ValidationError
            
        except serializers.ValidationError as e:
            # Catch validation errors and return them in the response
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    """
    if request.method == 'POST':
        cricketer_batting_serializer = CricketerSerializer(
            data=request.data.get('cricketer'))
        batting_record_serializer = BattingSerializer(
            data=request.data.get('batting'))
        bowling_record_serializer = BowlingSerializer(
            data=request.data.get('bowling'))

        # Validate all serializers individually
        cricketer_batting_serializer.is_valid(raise_exception=True)
        batting_record_serializer.is_valid(raise_exception=True)
        bowling_record_serializer.is_valid(raise_exception=True)

        # Save the valid data to database
        # Validate the data in all three serializers

        cricketer_batting_serializer.save()
        batting_record_serializer.save()
        bowling_record_serializer.save()

        return Response("Data Saved Successfully", status=status.HTTP_201_CREATED)

    else:
        errors = {}

        # Extract errors from each serializer
        if not cricketer_batting_serializer.is_valid():
            errors['cricketer'] = [
                {'field': field, 'message': msg}
                for field, msg in cricketer_batting_serializer.errors.items()
            ]
        """ #similar
        error_dict = {}
        for field, errors in serializer.errors.items():
            error_dict[field] = errors
        """
        if not batting_record_serializer.is_valid():
            errors['batting'] = [
                {'field': field, 'message': msg}
                for field, msg in batting_record_serializer.errors.items()
            ]
        if not bowling_record_serializer.is_valid():
            errors['bowling'] = [
                {'field': field, 'message': msg}
                for field, msg in bowling_record_serializer.errors.items()
            ]

        # If there are errors, return them in a structured response
        if errors:
            return Response({'message': 'Validation errors', 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)



        



@api_view(['GET'])
def get_all_cricketers(request):

    if request.method == "GET":

        cricketers = Cricketers.objects.all()
        cricketer_batting_serializer = CricketerSerializer(cricketers, many =True)

        batting_record = Batting_Record.objects.all()
        batting_record_serializer = BattingSerializer(batting_record, many=True)

        bowling_record = Bowling_Record.objects.all()
        bowling_record_serializer = BowlingSerializer(bowling_record, many=True)

        response_data = {
            cricketer_batting_serializer.data,
            batting_record_serializer.data,
            bowling_record_serializer.data,
        }
        return Response(response_data,status=status.HTTP_200_OK)



@api_view(['GET','POST','DELETE'])
def manipulate_player_bio(request,player_id):
    cricketer = get_object_or_404(Cricketers,pk=player_id)

    if request.method == 'GET':
        cricketer_serializer = CricketerSerializer(cricketer)
        return Response(cricketer_serializer.data)
    
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
    

@api_view(['GET', 'POST', 'DELETE'])
def manipulate_player_batting(request, player_id):
    cricketer_batting = get_object_or_404(Batting_Record, pk=player_id)

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

    if request.method == 'DELETE':
        cricketer_batting.delete()
        return Response("Cricketer Batting Profile Deleted", status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'DELETE'])
def manipulate_player_bowling(request, player_id):
    cricketer_bowling = get_object_or_404(Bowling_Record, pk=player_id)

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

    if request.method == 'DELETE':
        cricketer_bowling.delete()
        return Response("Cricketer Bowling Profile Deleted", status=status.HTTP_204_NO_CONTENT)
    




        
    
        
    








    



