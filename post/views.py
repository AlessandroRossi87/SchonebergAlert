from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import NewPostForm
from .models import Post


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post/detail.html', {
        'post': post
    })


@login_required
def new(request):
    form = NewPostForm()

    return render(request, 'post/form.html', {
        'form': form
    })
