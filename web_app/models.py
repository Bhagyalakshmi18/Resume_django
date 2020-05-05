from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class UploadPdf(models.Model):
#     jobrole = models.CharField(max_length=100)
    resumes = models.FileField(upload_to='resumes/', blank=True, null=True)
        
#     def __str__(self):
#         return self.jobrole
    
class UploadKeyword(models.Model):
    keyword = models.FileField(upload_to='keyword/', blank=True, null=True)
    