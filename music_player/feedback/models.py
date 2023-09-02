from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from music.models import Song
from account.models import User

# Create your models here.
class Like(BaseModel):
    # _id = models.BigIntegerField(primary_key=True) 
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(BaseModel):
    text = models.TextField(_("Comment"))
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    