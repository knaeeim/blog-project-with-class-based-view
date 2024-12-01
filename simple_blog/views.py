from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def homepage(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        categories = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = categories)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'categories' : categories})