from rest_framework import serializers

from .models import *


class MODE2LNAMESerializer(serializers.ModelSerializer):
    class Meta:
        model = MODE2LNAME
        fields = '__all__'


class MODELNAMESerializer(serializers.ModelSerializer):
    name = MODE2LNAMESerializer(many=True, required=False)

    class Meta:
        model = MODELNAME
        fields = '__all__'

