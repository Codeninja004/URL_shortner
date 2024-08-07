from django.urls import path
from .views import urlshort,red_url

urlpatterns = [
    path('',urlshort,name='home'),
     path("<str:pk>/",red_url,name='redirect')
]
