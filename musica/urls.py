from django.urls import path
from . import views

urlpatterns = [
    path('artistas/',views.lista_artistas, name='lista_artistas'),
    path('artista/<int:pk>',views.detalle_artista, name='detalle_artista'),
]
