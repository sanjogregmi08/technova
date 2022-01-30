from django import forms
from seller.models import Products1

class ProductForm(forms.ModelForm):
    class Meta:
        model =Products1
        fields="__all__"