from django.urls import path
from .views import index, setacookie
from . import views

app_name = "aula3"

urlpatterns =[
    path('', index),
    path('cookie', setacookie),
    path('cat/<int:code>', views.cat_status),
    path('get/', views.show_get_values),
    path('post/', views.show_post_values),
]
