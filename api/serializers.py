from pyexpat import model
from rest_framework import serializers
from .models import Mobile, Rating

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
