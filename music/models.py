# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='static/images/')


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.id})

    def _str_(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.id})
