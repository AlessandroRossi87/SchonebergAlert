from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewPostForm, EditPostForm, CommentForm
from .models import Category, Post, Comment


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

    return render(request, 'post/detail.html', {
        'post': post
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


@login_required
def comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect('post:detail', pk=post.id)

    else:
        form = CommentForm()

    return render(request, 'post/form.html', {
        'form': form
    })
