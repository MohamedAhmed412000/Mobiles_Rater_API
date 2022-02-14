from django.shortcuts import render
from rest_framework import viewsets
from .models import Mobile, Rating
from .serializers import MobileSerializer, RatingSerializer, UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token

# Create your views here.
class MobileViewsets(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods= ['post'], detail= True)
    def rate_mobile(self, request, pk=None):
        if 'stars' in request.data:
            # username = request.data['username']
            # user = User.objects.get(username= username)
            user = request.user
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

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        jsonResponse = {
            "message": "You shouldn't create mobile rating from here."
        }
        return Response(jsonResponse, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        jsonResponse = {
            "message": "You shouldn't update mobile rating from here."
        }
        return Response(jsonResponse, status=status.HTTP_400_BAD_REQUEST)

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permissions_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer= serializer)
        token, created = Token.objects.get_or_create(user= serializer.instance)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = {
            "message": "You can't get list of user."
        }
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
