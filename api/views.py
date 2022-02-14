from django.shortcuts import render
from rest_framework import viewsets
from .models import Mobile, Rating
from .serializers import MobileSerializer, RatingSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.
class MobileViewsets(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    @action(methods= ['post'], detail= True)
    def rate_mobile(self, request, pk=None):
        if 'stars' in request.data:
            username = request.data['username']
            user = User.objects.get(username= username)
            mobile = Mobile.objects.get(id=pk)
            stars = request.data['stars']
            try:
                # Update rate
                rating = Rating.objects.get(user = user.id, mobile = mobile.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                jsonResponse = {
                    "message": "Phone rate updated",
                    "result": serializer.data
                }
                return Response(jsonResponse, status=status.HTTP_202_ACCEPTED)
            except:
                # Create rate
                rating = Rating.objects.create(user=user, mobile=mobile, stars=stars)
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                jsonResponse = {
                    "message": "Phone rate added",
                    "result": serializer.data
                }
                return Response(jsonResponse, status=status.HTTP_201_CREATED)
        else:
            jsonResponse = {
                "message": "Stars aren't provided."
            }
            return Response(jsonResponse, status=status.HTTP_400_BAD_REQUEST)

class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
