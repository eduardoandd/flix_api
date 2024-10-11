from django.contrib import admin
from django.urls import path
from genres.views import *
from actors.views import *
from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(),name='genre_create_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(),name='genre_datail_view'),
    
    path('actor/', ActorCreateListView.as_view(),name='actor_create_list'),
    path('actor/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(),name='actor_datail_view'),
    
    path('movies/', MovieCreateListView.as_view(),name='movie_create_list'),
    path('movies/<int:pk>/', MovieRetrieverUpdateDestroyView.as_view(),name='movies_datail_view'),
    
]
