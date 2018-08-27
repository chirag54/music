# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Album, Song
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_Album_list'
    print('hii')

    def get_queryset(self):
        print("queryset")
        """Return the last five published questions."""
        return Album.objects.all()


class AlbumCreate(CreateView):
    models = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'album_form.html'
    print("album create")
    print(fields[3:4])

    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()


class AlbumUpdate(UpdateView):
    models = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'album_form.html'
    print("album create")

    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()


class SongAdd(CreateView):
    models = Song
    fields = ['album', 'file_type', 'song_title']
    template_name = 'song_form.html'
    print("song add")

    def get_queryset(self):
        """Return the last five published questions."""
        return Song.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'detail.html'


def search(request):
        album_list = Album.objects.all()
        quuery = request.GET.get("q")
        print('search')
        if quuery:
            album_list = album_list.filter(artist__icontains=quuery)

        context = {'latest_Album_list': album_list}
        return render(request, 'index.html', context)
