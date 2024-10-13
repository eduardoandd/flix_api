from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import *

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Actor.objects.all()
    serializer_class= ActorSerializer
    
class ActorRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Actor.objects.all()
    serializer_class=ActorSerializer

