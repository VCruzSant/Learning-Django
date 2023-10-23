from django.shortcuts import render


# Create your views here.
def blog(request):
    print('index')
    return render(
        request,
        'blog/index.html'
    )
