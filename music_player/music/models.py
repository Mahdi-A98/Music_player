# IN the name of GOD
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from accounts.models import User, Artist

# Create your models here.
class Gener(BaseModel):
    name = models.CharField(verbose_name=_("Music gener name"), max_length=50)


class Song(BaseModel):
    title = models.CharField(_("Song title"), max_length=50)
    gener = models.ForeignKey(Gener, on_delete=models.SET_NULL)
    cover = models.ImageField(_("Song cover"), upload_to='songs/covers/')
    artists = models.ManyToManyField(Artist)
    audio_file = models.FileField(_("Song file"), upload_to='songs/files/')
    duration = models.DurationField(_("Song Duration"))


class PlayList(BaseModel):
    title = models.CharField(_("PlayList title"), max_length=50)
    description = models.TextField(_("PlayList Description"))
    songs = models.ManyToManyField(Song)
    owner = models.ForeignKey(User, verbose_name=_("PlayList owner"), on_delete=models.CASCADE)
