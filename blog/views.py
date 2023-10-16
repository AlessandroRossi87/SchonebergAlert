from django.shortcuts import render, redirect

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
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })
