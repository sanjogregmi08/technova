from django import  forms
from c_profile.models import Delivery

class DeliveryForm(forms.ModelForm):
    class Meta:
        model= Delivery
        fields = "__all__"