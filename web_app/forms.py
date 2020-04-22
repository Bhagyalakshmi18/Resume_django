from django import forms
from .models import UploadPdf

class ResumeUpload(forms.ModelForm):
    class Meta:
        model = UploadPdf
        fields = ('jobrole', 'resumes')
        
    