from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mybase/', views.mybase, name='mybase'),
]