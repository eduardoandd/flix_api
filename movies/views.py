from django.shortcuts import render
from movies.models import *
from rest_framework import generics
from movies.serializers import *

class MovieCreateListView(generics.ListCreateAPIView):
    queryset= Movie.objects.all()
    serializer_class= MovieSerializer
    
class MovieRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer