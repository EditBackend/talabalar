from rest_framework import serializers
from .models import *

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'


class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'


class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = '__all__'


class TolovQaytarishSerializer(serializers.ModelSerializer):
    class Meta:
        model = TolovQaytarish
        fields = '__all__'
