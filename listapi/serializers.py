from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User,AddressDetails

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'

