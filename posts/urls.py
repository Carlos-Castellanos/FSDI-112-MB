from django.urls import path
from .views import (
    PostDetailView, 
    PostListView, 
    PostCreateView
)

urlpatterns = [
    path('',PostListView.as_view(), name="posts_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
     path('new/', PostCreateView.as_view(), name="post_new"),

]