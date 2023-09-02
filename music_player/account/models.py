from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
# Create your models here.


class BaseUserModel(AbstractUser):
    image = models.ImageField(verbose_name=_("Product Image"), null=True, blank=True,  upload_to='profile/images/')
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    class Meta:
        abstract = True

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/> ')

class User(BaseUserModel):
    email = models.EmailField(_("email address"), null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=(("N", "Normal"), ("V", "VIP")))
    
