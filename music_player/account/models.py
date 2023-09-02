from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(_("email address"), null=True, blank=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='profile/images/')
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    def img_preview(self):
        if self.photo:
            return mark_safe(f'<img src = "{self.photo.url}" width = "150" height="150"/> ')