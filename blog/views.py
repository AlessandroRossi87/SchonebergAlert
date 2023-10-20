from django.shortcuts import render, redirect
from django.views import generic, View

from post.models import Category, Post

from .forms import SignupForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    paginate_by = 8


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
