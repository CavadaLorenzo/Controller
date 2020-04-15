from django import forms
from .models import TransferRequest


class TransferRequestForm(forms.ModelForm):
    class Meta:
       model = TransferRequest
       fields= ['view_count', 'time_span']
