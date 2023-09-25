from django import forms
from indexapp.models import ContactUSMessage


class CreateContactUSForm(forms.ModelForm):
    class Meta:
        model = ContactUSMessage
        fields = ['name','email', 'subject', 'message']
