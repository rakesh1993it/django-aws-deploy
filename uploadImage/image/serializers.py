from rest_framework import serializers
from image.models import *
import json

class hotelSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Hotel
        fields ='__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"