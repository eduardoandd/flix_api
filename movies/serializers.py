from actors.models import Actor
from genres.models import Genre
from movies.models import Movie
from rest_framework import serializers

    

class MovieModelSerializer(serializers.ModelSerializer):
    
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=Movie
        fields='__all__'
        
    def get_rate(self,obj):
        reviews= obj.review.all()
        
        if reviews:
            sum_reviews=0
            for review in reviews:
                sum_reviews +=review.stars          
                
            mean= round(sum_reviews / reviews.count(),1)
            
            return mean
    
    def validate_realease_data(self,value):
        if value.year <1930:
            raise serializers.ValidationError('A dara de lançamento não pode ser inferior a 1990.')
        
        return value
    
    def validate_resume(self,value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo limitado á 200 caracteres.')
        
    
        
        