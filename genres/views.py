from django.http import JsonResponse
from genres.models import Genre


# END POINT ALL
def genre_view(request):
    genres = Genre.objects.all() # SELECT * FROM GENRES
    data = [{'id': genre.id, 'name':genre.name} for genre in genres]
    
    return JsonResponse(data, safe=False)
