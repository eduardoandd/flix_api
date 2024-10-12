from django.urls import path

from movies.views import *

urlpatterns=[
    path('movies/', MovieCreateListView.as_view(),name='movie_create_list'),
    path('movies/<int:pk>/', MovieRetrieverUpdateDestroyView.as_view(),name='movie_datail_view'),
]