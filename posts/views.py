# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post
# Create your views here.

class PostListView(ListView):
    template_name = "posts/list.html"    ##check the dir name "postSSS"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"  ##check the dir name "postSSS"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"  ##check the dir name "postSSS"
    model = Post
    fields = ["title","subtitle","body"]   ##verify the fieldname's in posts/model.py