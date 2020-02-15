from django.urls import path, include
from .views import index, setacookie, redireciona

urlpatterns =[
   path('', index),
    path('cookie', setacookie),
    path('uol', redireciona)
]
