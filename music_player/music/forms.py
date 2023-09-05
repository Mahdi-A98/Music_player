# in the name of GOD

from django import forms

from .models import PlayList, Song, Gener

class CreatePlayListForm(forms.ModelForm):

    class Meta:
        model = PlayList
        fields = ['title', 'description', 'songs']