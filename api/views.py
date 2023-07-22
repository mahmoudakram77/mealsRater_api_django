from django.shortcuts import render 
from rest_framework import viewsets
from .models import *
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework import response , status 
from django.contrib.auth.models import User
class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            stars = request.data['stars']
            user = User.objects.get(username=username)

            try:
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializer(rate)
                json = {
                    'message': 'meal rate updated',
                    'result': serializer.data
                }
                return Response(json, status.HTTP_200_OK)

            except Rating.DoesNotExist:
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating)
                json = {
                    'message': 'meal rated successfully',
                    'result': serializer.data
                }
                return Response(json, status.HTTP_201_CREATED)

        else:
            json = {
                "message": "stars not provided"
            }
            return Response(json, status.HTTP_400_BAD_REQUEST)
     
class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class=RatingSerializer




# Create your views here.
