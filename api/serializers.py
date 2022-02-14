from pyexpat import model
from rest_framework import serializers
from .models import Mobile, Rating

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": { "write_only": True, "required": True }
        }

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     token = Token.objects.create(user = user)
    #     return token

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'company', 'name', 'price', 'no_of_ratings', 'avg_ratings']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
