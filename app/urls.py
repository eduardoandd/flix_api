from django.contrib import admin
from django.urls import path,include
from genres.views import *
from actors.views import *
from movies.views import *
from reviews.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('authentication.urls')),    
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('reviews.urls')),
    
]
