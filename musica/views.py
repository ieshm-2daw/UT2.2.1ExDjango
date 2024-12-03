from django.shortcuts import render, get_object_or_404
from .models import Artista,Album,Cancion

# Create your views here.
def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'musica/lista_artistas.html',{"artistas":artistas})
def detalle_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'musica/detalle_artista.html',{"artista":artista})