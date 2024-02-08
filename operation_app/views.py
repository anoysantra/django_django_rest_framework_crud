from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cricketers, Batting_Record, Bowling_Record
from .serializers import  CricketerSerializer, BattingSerializer, BowlingSerializer 
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def add_get_cricketers(request):

    if request.method == 'POST':
        cricketer_serializer = CricketerSerializer(data=request.data.get('cricketer'))
        batting_record_serializer = BattingSerializer(data=request.data.get('batting'))
        bowling_record_serializer = BowlingSerializer(data=request.data.get('bowling'))

        if (cricketer_serializer.is_valid() and batting_record_serializer.is_valid and 
            bowling_record_serializer.is_valid()):
            # Saving the valid data to database
            # Validate the data in all three serializers
            cricketer_serializer.save()
            batting_record_serializer.save()
            bowling_record_serializer.save()
            return Response("Data Saved Successfully", status=status.HTTP_201_CREATED)
        else:
            #if any error is encountered or serializers not valid
            errors = {
                'cricketer_errors':  cricketer_serializer.errors,
                'batting_errors' :   batting_record_serializer.errors,
                'bowling_errors' :   bowling_record_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":

        cricketers = Cricketers.objects.all()
        cricketer_serializer = CricketerSerializer(cricketers, many =True)

       #.....to be continued




    



