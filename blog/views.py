from django.shortcuts import render


# Create your views here.


def blog(request):
    print('index')

    context = {
        'text': 'This is Blog',
        'title': 'Blog'
    }

    return render(
        request,
        'blog/index.html',
        context
    )
