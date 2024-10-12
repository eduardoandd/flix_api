from django.contrib import admin
from django.urls import path,include
from genres.views import *
from actors.views import *
from movies.views import *
from reviews.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1', include('genres.urls')),
    
    
    path('actor/', ActorCreateListView.as_view(),name='actor_create_list'),
    path('actor/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(),name='actor_datail_view'),
    
    path('movie/', MovieCreateListView.as_view(),name='movie_create_list'),
    path('movie/<int:pk>/', MovieRetrieverUpdateDestroyView.as_view(),name='movie_datail_view'),
    
    path('review/', ReviewCreateListView.as_view(),name='review_create_list'),
    path('review/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(),name='review_datail_view'),
    
]
