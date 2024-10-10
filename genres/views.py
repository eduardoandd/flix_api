from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



# END POINT 
@csrf_exempt
def genre_create_list_view(request):
    
    if request.method == 'GET':
        genres = Genre.objects.all() # SELECT * FROM GENRES
        data = [{'id': genre.id, 'name':genre.name} for genre in genres]
        
        return JsonResponse(data, safe=False)
    else:
        data = json.loads(request.body.decode('utf-8')) # pega o corpo da requisição
        # print(data)
        new_genre=Genre(name=data['name'])
        # print(new_genre)
        new_genre.save()
        
        return JsonResponse({'id': new_genre.id, 'name':new_genre.name},status=201)
        
@csrf_exempt
def genre_detail_view(request, pk):
    # genre = Genre.objects.get(pk=pk)
    genre= get_object_or_404(Genre,pk=pk)
    data = {'id': genre.id, 'name': genre.name}
    
    return JsonResponse(data)

