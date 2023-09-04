from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
# Create your models here.


class User(AbstractUser):
    image = models.ImageField(verbose_name=_("Product Image"), null=True, blank=True,  upload_to='profile/images/')
    email = models.EmailField(_("email address"),unique=True, null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=(("N", "Normal"), ("V", "VIP")))
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/> ')


class Band(models.Model):
    name = models.CharField(max_length=50)

class Artist(models.Model):
    first_name = models.CharField(_("Artist first name"), max_length=50)
    last_name = models.CharField(_("Artist last name"), max_length=50)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(_("Artist Image"), upload_to='Artists/images')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


