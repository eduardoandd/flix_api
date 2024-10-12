from django.urls import path

from . import views

urlpatterns=[
    path('genre/', views.GenreCreateListView.as_view(),name='genre_create_list'),
    path('genre/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(),name='genre_datail_view'),  
]

