from django import forms
from django.forms import ClearableFileInput
from .models import UploadPdf, UploadKeyword

class ResumeUpload(forms.ModelForm):
    class Meta:
        model = UploadPdf
        fields = ['resumes']
        widgets = {
            'resumes': ClearableFileInput(attrs={'multiple': True}),
        }
        
class KeywordUpload(forms.ModelForm):
    class Meta:
        model = UploadKeyword
        fields = ['keyword']