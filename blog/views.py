from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Post, Comment
from .forms import SignupForm, NewPostForm, EditPostForm, CommentForm


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


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    posts = Post.objects.all()

    if category_id:
        posts = posts.filter(category_id=category_id)

    if query:
        posts = posts.filter(Q(title__icontains=query)
                             | Q(text__icontains=query))

    return render(request, 'post/browse.html', {
        'posts': posts,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    comments = post.comments.all()

    return render(request, 'post/detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


def category(request, category_name):
    category = get_object_or_404(Category, id=category_name)
    posts = Post.objects.filter(category=category, active=True)

    return render(request, 'home.html', {
        'category': category,
        'posts': posts,
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect('post:detail', pk=post.id)
    else:
        form = NewPostForm()

    return render(request, 'post/form.html', {
        'form': form,
        'title': 'Post new Alert',
    })


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    post.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post:detail', pk=post.id)
    else:
        form = EditPostForm(instance=post)

    return render(request, 'post/form.html', {
        'form': form,
        'title': 'Edit Alert',
    })
