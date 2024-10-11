from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    
    
    


# # GET E POST
# @csrf_exempt
# def genre_create_list_view(request):
    
#     if request.method == 'GET':
#         genres = Genre.objects.all() # SELECT * FROM GENRES
#         data = [{'id': genre.id, 'name':genre.name} for genre in genres]
        
#         return JsonResponse(data, safe=False)
#     else:
#         data = json.loads(request.body.decode('utf-8')) # pega o corpo da requisição
#         # print(data)
#         new_genre=Genre(name=data['name'])
#         # print(new_genre)
#         new_genre.save()
        
#         return JsonResponse({'id': new_genre.id, 'name':new_genre.name},status=201)
    

# DELETE E UPDATE E GETBYID 
@csrf_exempt
def genre_detail_view(request, pk):
    
    # genre = Genre.objects.get(pk=pk)
    genre= get_object_or_404(Genre,pk=pk)
    
    if request.method ==  'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name= data['name']
        genre.save()
        
        return JsonResponse({'id': pk, 'name':genre.name})
    
    elif request.method == 'DELETE':
        
        genre.delete()
        return JsonResponse({'message': 'Genero excluido com sucesso.'}, status=204)
        
    

