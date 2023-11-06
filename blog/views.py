from blog.data import posts
from django.shortcuts import render
from django.http import HttpRequest, Http404
from typing import Any

# Create your views here.


def blog(request):
    print('index')

    context = {
        'text': 'This is Blog',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    print('index')

    context = {
        'post': found_post,
        'title': found_post['id']
    }

    return render(
        request,
        'blog/post.html',
        context
    )
