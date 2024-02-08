from rest_framework import serializers
from . models import Cricketers , Batting_Record , Bowling_Record

class  CricketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketers
        fields='__all__'

class BattingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batting_Record
        fields='__all__'


class BowlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bowling_Record
        fields = '__all__'
