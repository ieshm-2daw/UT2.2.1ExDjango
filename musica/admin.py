from django.contrib import admin
from .models import Album, Artista, Cancion

# Register your models here.
admin.site.register(Album)
admin.site.register(Artista)
admin.site.register(Cancion)