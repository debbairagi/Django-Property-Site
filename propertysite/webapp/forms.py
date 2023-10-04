from crudapp.models import Property
from django import forms
class PropertyEntryForm(forms.ModelForm):
    # property_pics = forms.FileField(
    #     label="Property Pics",
    #     widget=forms.ClearableFileInput(attrs={'multiple':True}),
    # )
    class Meta:
        model = Property
        fields = "__all__"