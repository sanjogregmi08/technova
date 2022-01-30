from dataclasses import fields
from django import forms
from feedback.models import Feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"