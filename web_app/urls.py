from django.urls import path
from .views import (
    PostListView,
    PostDetailView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='resume-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='resume-about'),
    path('pdfs/', views.store_pdf, name='store_pdf'),
    path('pdfs/upload/', views.upload_pdf, name='upload_pdf'),
    
]


