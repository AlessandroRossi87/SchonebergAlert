from django.shortcuts import render

from post.models import Category, Post


def home(request):
    posts = Post.objects.filter()[0:6]
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'categories': categories,
        'posts': posts,
    })

def contact(request):
    return render(request, 'contact.html', {})