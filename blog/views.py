from django.shortcuts import render

from post.models import Category, Post

from .forms import SignupForm


def home(request):
    posts = Post.objects.filter()[0:6]
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'categories': categories,
        'posts': posts,
    })


def contact(request):
    return render(request, 'contact.html', {})


def signup(request):
    form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })
