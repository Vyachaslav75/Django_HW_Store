from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mybase/', views.mybase, name='mybase'),
    path('get_products/<int:id>/<int:days>', views.get_products, name='get_products'),
]