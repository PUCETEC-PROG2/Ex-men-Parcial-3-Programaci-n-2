from django.http import HttpResponse
from django.template import loader
from .models import Álbum, Artista
from album_manager.forms import ArtistaForm, ÁlbumForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login_form.html"
    
def index(request):
    albums = Álbum.objects.all()
    artistas = Artista.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'albums': albums,
        'artistas' : artistas
    }, request))
    
def artistas (request):
    artistas = Artista.objects.all()
    template = loader.get_template('artista.html')
    return HttpResponse(template.render({
        'artistas' : artistas
    }, request))
    
def info_album(request, album_id):
    albums = Álbum.objects.get(pk = album_id)
    template = loader.get_template('info_album.html')
    context = {
        'album': albums
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_album(request):
    if request.method == "POST":
        form = ÁlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
        else:
            print(form.errors)
    else:
        form = ÁlbumForm()
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def edit_album(request, album_id):
    album = Álbum.objects.get(pk = album_id)
    if request.method == "POST":
        form = ÁlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ÁlbumForm(instance=album)
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def delete_album(request, album_id):
    album = Álbum.objects.get(pk = album_id)
    album.delete()
    return redirect('album_manager:index')


@login_required
def add_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm()
    
    return render(request, 'artista_form.html', {'form': form})

@login_required
def edit_artista(request, artista_id):
    artista = Artista.objects.get(pk = artista_id)
    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm(instance=artista)
    
    return render(request, 'artista_form.html', {'form': form})

@login_required
def delete_artista(request, artista_id):
    artista = Artista.objects.get(pk = artista_id)
    artista.delete()
    return redirect('album_manager:index')