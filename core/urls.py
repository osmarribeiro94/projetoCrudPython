from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='index'),
    path('criar', views.criar, name='criar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
