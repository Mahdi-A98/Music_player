from django.contrib import admin
from .models import User, Artist, Band
# Register your models here.

admin.site.register(User)
admin.site.register(Band)
admin.site.register(Artist)