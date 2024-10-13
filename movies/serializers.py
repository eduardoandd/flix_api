from rest_framework import serializers
from django.db.models import Avg

from actors.models import Actor
from genres.models import Genre
from movies.models import Movie


    

class MovieModelSerializer(serializers.ModelSerializer):
    
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=Movie
        fields='__all__'
        
    def get_rate(self,obj):
        
        rate=obj.review.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)
        
        return None
        
    
    def validate_realease_data(self,value):
        if value.year <1930:
            raise serializers.ValidationError('A dara de lançamento não pode ser inferior a 1990.')
        
        return value
    
    def validate_resume(self,value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo limitado á 200 caracteres.')
        
    
        
        