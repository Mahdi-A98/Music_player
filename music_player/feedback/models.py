from django.db import models
from music.models import Song
from account.models import User
from core.models import BaseModel

# Create your models here.
class Like(BaseModel):
    # _id = models.BigIntegerField(primary_key=True) 
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(BaseModel):
    text = models.TextField(_("Comment"))
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)