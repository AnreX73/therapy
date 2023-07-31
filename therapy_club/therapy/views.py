from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from therapy.models import Services, Graphics, Coaches, Post, ServiceCategory, Gallery, Contacts, Commercial


def index(request):
    main_service = ServiceCategory.objects.get(title='Занятие с тренером')
    services = Services.objects.exclude(title='х-запасной порт')
    service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')[1:]
    contacts = Contacts.objects.exclude(title='Карта')
    contacts_map = Contacts.objects.get(title='Карта')
    main_image = Graphics.objects.get(title='картинка на главную')
    commerc = Commercial.objects.filter(is_published=True).order_by('-pk')[:1]
    logo = Graphics.objects.get(title='лого вместо фото')
    service_cats_all = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')

    context = {
        'main_service': main_service,
        'title': 'Главная страница',
        'services': services,
        'service_cats': service_cats,
        'contacts': contacts,
        'contacts_map': contacts_map,
        'main_image': main_image,
        'commerc': commerc,
        'logo': logo,
        'service_cats_all':service_cats_all

    }

    return render(request, 'therapy/index.html', context=context)


def service(request, slug):
    service_item = get_object_or_404(Services, slug=slug)
    context = {
        'title': service_item.title,
        'service': service_item
    }
    return render(request, 'therapy/service.html', context=context)


def rules(request):
    rules = Post.objects.get(title='Правила посещения')

    context = {
        'rules': rules,

    }

    return render(request, 'therapy/rules.html', context=context)


class Coaches(ListView):
    logo = Graphics.objects.get(title='логотип')
    model = Coaches
    template_name = 'therapy/coach_list.html'
    context_object_name = 'coaches'
    extra_context = {
        'title': 'Наша команда',
        'logo': logo

    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
