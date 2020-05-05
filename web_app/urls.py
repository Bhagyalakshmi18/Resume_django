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
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('keyword/', views.upload_keyword, name='upload_keyword'),
    
]


