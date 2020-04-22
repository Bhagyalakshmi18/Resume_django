from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class UploadPdf(models.Model):
    jobrole = models.TextField()
    resumes = models.FileField(upload_to='resumes/', blank=True, null=True)
        
    def __str__(self):
        return self.jobrole
    
    
# from django import forms

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     