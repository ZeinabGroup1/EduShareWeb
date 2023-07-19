from django.shortcuts import render
from .models import Blog




def main(request):
    blog = Blog.objects.all()
    return render(request, 'home/main.html', {'blog': blog})

# Create your views here.

# blog/views.py



# def detail(request, blog_id):
#     blog_post = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog_post': blog_post})

