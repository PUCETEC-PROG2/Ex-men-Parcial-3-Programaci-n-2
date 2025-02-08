# Ingresar tus URLs de la app aquí

from django.urls import path
from . import views

app_name = 'album_manager'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('artistas/', views.artistas, name='artistas'),
    path("add_album/", views.add_album, name="add_album"),
    path("add_artista/", views.add_artista, name="add_artista"),
    path("editar_album/<int:album_id>/", views.edit_album, name="editar_album"),
    path("editar_artista/<int:artista_id>/", views.edit_artista, name="editar_artista"),
    path("eliminar_album/<int:album_id>/", views.delete_album, name="eliminar_album"),
    path("eliminar_artista/<int:artista_id>/", views.delete_artista, name="eliminar_artista"),
    path("<int:album_id>/", views.info_album, name="informacion_del_album"),
]