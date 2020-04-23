from django import forms
from .models import TransferRequest


class TransferRequestForm(forms.ModelForm):
    """
    Simple class for build a form used to create new TransferRequest.
    """
    class Meta:
       model = TransferRequest
       fields= ['view_count', 'time_span']
