from django.shortcuts import render

from therapy.models import Services


def index(request):
    context = {
        'title': 'Главная страница',

    }

    return render(request, 'therapy/index.html', context=context)
