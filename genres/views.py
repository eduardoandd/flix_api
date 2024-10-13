from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated

#GET ALL AND POST
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer

# GET BY ID, PUT, DELETE
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Genre.objects.all()
    serializer_class= GenreSerializer
    
