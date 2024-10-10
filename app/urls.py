
from django.contrib import admin
from django.urls import path
from genres.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_create_list_view,name='genre_create_list'),
    path('genres/', genre_create_list_view,name='genre_create_list'),
    path('genres/<int:pk>/', genre_detail_view,name='genre_datail_view'),
]
