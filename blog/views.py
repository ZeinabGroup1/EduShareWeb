from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Blog



def main(request):
    blog = Blog.objects.all()
    return render(request, 'home/main.html', {'blog': blog})


def detail(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_post': blog_post})


