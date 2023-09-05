# IN the name of GOD
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from account.models import User, Artist

# Create your models here.
class Gener(BaseModel):
    name = models.CharField(verbose_name=_("Music gener name"), max_length=50)

    def __str__(self):
        return self.name

class Song(BaseModel):
    title = models.CharField(_("Song title"), max_length=50)
    gener = models.ForeignKey(Gener, null=True, blank=True, on_delete=models.SET_NULL)
    cover = models.ImageField(_("Song cover"), null=True, blank=True, upload_to='songs/covers/')
    artists = models.ManyToManyField(Artist)
    audio_file = models.FileField(_("Song file"), upload_to='songs/files/')
    duration = models.DurationField(_("Song Duration"), null=True, blank=True, )

    def __str__(self):
        return self.title


class PlayList(BaseModel):
    title = models.CharField(_("PlayList title"), max_length=50)
    description = models.TextField(_("PlayList Description"),  null=True, blank=True, )
    songs = models.ManyToManyField(Song, null=True, blank=True)
    owner = models.ForeignKey(User, verbose_name=_("PlayList owner"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
