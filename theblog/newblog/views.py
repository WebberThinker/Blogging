from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"

class BlogView(ListView):
    model = Post
    template_name = "blogs.html"

class DetailPageView(DetailView):
    model = Post
    template_name = "detail_page.html"

