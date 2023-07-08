from django.shortcuts import render

from therapy.models import Services, Graphics, Coaches


def index(request):
    logo = Graphics.objects.get(title='логотип')
    coaches = Coaches.objects.all()
    main_image = Graphics.objects.get(title='картинка на главную')
    
    context = {
        'title': 'Главная страница',
        'logo': logo,
        'coaches': coaches,
        'main_image':main_image

    }

    return render(request, 'therapy/index.html', context=context)
