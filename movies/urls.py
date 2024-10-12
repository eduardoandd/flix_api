from django.urls import path

from actors.views import *


urlpatterns=[
    path('actors/', ActorCreateListView.as_view(),name='actor_create_list'),
    path('actors/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(),name='actor_datail_view'),
]