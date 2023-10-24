from django.shortcuts import render


# Create your views here.


def home(request):
    print('index')

    context = {
        'text': 'This is Home',
        'title': 'Home'
    }

    return render(
        request,
        'home/index.html',
        context
    )
