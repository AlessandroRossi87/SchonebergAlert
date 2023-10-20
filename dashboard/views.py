from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from blog.models import Post


@login_required
def index(request):
    posts = Post.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'posts': posts,
    })
