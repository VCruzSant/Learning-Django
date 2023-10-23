from django.shortcuts import render


# Create your views here.
def home(request):
    print('index')
    return render(
        request,
        'home/index.html'
    )
