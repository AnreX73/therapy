from django.shortcuts import render

from therapy.models import Services, Graphics, Coaches


def index(request):
    logo = Graphics.objects.get(title='логотип')
    image = Coaches.objects.get(pk=1)
    context = {
        'title': 'Главная страница',
        'logo': logo,
        'coach_photo': image,

    }

    return render(request, 'therapy/index.html', context=context)
