from django import forms
from .models import Persona

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields =[
            "link_playlist",
        ]