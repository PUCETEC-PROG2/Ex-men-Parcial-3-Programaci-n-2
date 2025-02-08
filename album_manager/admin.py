from django.contrib import admin
from .models import Artista, Álbum
# Register your models here.
@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    pass

@admin.register(Álbum)
class ÁlbumAdmin(admin.ModelAdmin):
    pass