from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewPostForm
from .models import Post


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post/detail.html', {
        'post': post
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect('post:detail, pk=post.id')
    else:
        form = NewPostForm()

    return render(request, 'post/form.html', {
        'form': form
        'title': 'Post new Alert',
    })
