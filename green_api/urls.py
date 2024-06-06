from django.urls import path

from .views import index, index2


urlpatterns = [
    path('', index, name='home'),
    path('new_way/', index2, name='home2'),
]