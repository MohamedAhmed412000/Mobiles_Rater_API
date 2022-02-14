from django.shortcuts import render
from rest_framework import viewsets
from .models import Mobile, Rating
from .serializers import MobileSerializer, RatingSerializer

# Create your views here.
class MobileViewsets(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
