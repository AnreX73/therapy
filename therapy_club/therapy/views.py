from django.shortcuts import render

from therapy.models import Services, Graphics, Coaches, Post


def index(request):
    logo = Graphics.objects.get(title='логотип')
    coaches = Coaches.objects.all()
    main_image = Graphics.objects.get(title='картинка на главную')
    

    context = {
        'title': 'Главная страница',
        'logo': logo,
        'coaches': coaches,
        'main_image': main_image,
        'rules':rules

    }

    return render(request, 'therapy/index.html', context=context)

def rules(request):
    rules = Post.objects.get(title='Правила посещения')

    context = {

        'rules':rules

    }

    return render(request, 'therapy/rules.html', context=context)
    

