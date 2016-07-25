from django import forms
from .models import Pokemon
from plist.choices import *

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        element = forms.ChoiceField(choices=ELEMENTS, widget=forms.Select(attrs={'class':'dropdown'}))
        weakness = forms.ChoiceField(choices=ELEMENTS, widget=forms.Select(attrs={'class':'dropdown'}))
        name = forms.CharField(max_length=20)
        fields = ('name', 'element', 'weakness')
