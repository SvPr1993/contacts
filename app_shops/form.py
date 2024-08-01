from django import forms
from .models import Shops


class ShopsForm(forms.ModelForm):
    class Meta:
        model = Shops
        fields = ['brand', 'name', 'surname']
