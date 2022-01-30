from dataclasses import fields
from django import forms
from exchange.models import Exchange

class ExchangeForm(forms.ModelForm):
    class Meta:
        model= Exchange
        fields = "__all__"