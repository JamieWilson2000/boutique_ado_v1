from django.shortcuts import render


def index(request):
    """ A view that returns the index page"""

    return render(request, 'home/index.html')
