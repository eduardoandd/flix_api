from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.serializers import *
from movies.models import *


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset= Movie.objects.all()
    serializer_class= MovieModelSerializer
    
class MovieRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated)
    queryset=Movie.objects.all()
    serializer_class=MovieModelSerializer
    
  