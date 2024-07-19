from django import forms
from . import models

class fileUploadForm(forms.ModelForm):
    class Meta:
        model = models.Uploaded_file
        fields = ['title', 'file']