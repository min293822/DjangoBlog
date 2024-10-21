from django.shortcuts import render
from .models import Blog

def index(request):
  blogs = Blog.objects.all()
  context = {'blogs': blogs}
  return render(request, 'index.html', context)

def details(request, slug):
  blog = Blog.objects.get(slug=slug)
  context = {'blog': blog}
  return render(request, 'blog.html', context)
  
  