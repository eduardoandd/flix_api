from actors.models import Actor
from genres.models import Genre
from movies.models import Movie
from rest_framework import serializers

    

class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
    
    def validate_realease_data(self,value):
        if value.year <1990:
            raise serializers.ValidationError('A dara de lançamento não pode ser inferior a 1990.')
        
        return value
    
    def validate_resume(self,value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo limitado á 200 caracteres.')
        
        