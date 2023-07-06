from django.urls import path
from .views import BlogCreateView, BlogDetailView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
