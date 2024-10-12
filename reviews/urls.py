from django.urls import path

from reviews.views import *


urlpatterns=[
    path('reviews/', ReviewCreateListView.as_view(),name='review_create_list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(),name='review_datail_view'), 
]