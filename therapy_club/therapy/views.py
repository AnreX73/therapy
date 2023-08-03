from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from therapy.models import Services, Coaches, Post, ServiceCategory, Gallery, Contacts, Commercial


def index(request):
    main_service = ServiceCategory.objects.get(title='Занятие с тренером')
    services = Services.objects.exclude(title='х-запасной порт')
    # service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')[1:]
    contacts = Contacts.objects.exclude(title='Карта').exclude(title='мини-карта').exclude(title='средняя карта')
    contacts_map = Contacts.objects.get(title='Карта')
    contacts_mini_map = Contacts.objects.get(title='мини-карта')
    contacts_midi_map = Contacts.objects.get(title='средняя карта')

    commerc = Commercial.objects.filter(is_published=True).order_by('-pk')[:1]

    service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    for s_k in service_cats:
        if s_k.serv_category.count() < 3:
            obj_style = 'min_elem'

        else:
            obj_style = 'max_elem'
        print(obj_style)

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

        'contacts_mini_map': contacts_mini_map,
        'contacts_midi_map': contacts_midi_map
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
