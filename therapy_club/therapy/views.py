from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from therapy.models import Services, Coaches, Post, ServiceCategory, Gallery, Contacts, Commercial, Graphics, Abonements,ServicesGallery


def index(request):   
    services = Services.objects.exclude(title='х-запасной порт')
    logo = Graphics.objects.get(title='логотип')
    contacts = Contacts.objects.exclude(title='Карта').exclude(title='средняя карта').exclude(title='мини карта').exclude(title='микро карта')
    contacts_map = Contacts.objects.get(title='Карта')
    contacts_midi_map = Contacts.objects.get(title='средняя карта')
    contacts_mini_map = Contacts.objects.get(title='мини карта')
    contacts_micro_map = Contacts.objects.get(title='микро карта')
    main_image = Graphics.objects.get(title='картинка на главную')
    commerc = Commercial.objects.filter(is_published=True).order_by('-pk')[:1]
    commerc_count = Commercial.objects.filter(is_published=True).count()
    service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    
    
    context = {
        'title': 'Главная страница',
        'services': services,
        'service_cats': service_cats,
        'contacts': contacts,
        'contacts_map': contacts_map,
        'main_image': main_image,
        'commerc': commerc,
        'logo': logo,
        'contacts_midi_map':contacts_midi_map,
        'contacts_mini_map':contacts_mini_map,
        'contacts_micro_map':contacts_micro_map,
        'commerc_count':commerc_count

    }

    return render(request, 'therapy/index.html', context=context)


def service(request, slug):
    service_item = get_object_or_404(Services, slug=slug)
    service_abo = Abonements.objects.filter(service_link_id=service_item.id)
    logo = Graphics.objects.get(title='логотип')
    gallery = ServicesGallery.objects.filter(gallery_service_link_id=service_item.id)
    
    if service_item.cat_id == 2:
        word='одного занятия'
    elif service_item.cat_id == 4:
        word='одной программы'
    else:
        word='одного сеанса'
    context = {
        'title': service_item.title,
        'service': service_item,
        'service_abo':service_abo,
        'word':word,
        'logo':logo,
        'gallery':gallery
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


def prices(request):
    services = Services.objects.exclude(title='х-запасной порт')
    cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('pk')
    abonements = Abonements.objects.all().order_by('pk')

    context = {
        'services': services,
        'cats': cats,
        'abonements': abonements

    }

    return render(request, 'therapy/prices.html', context=context)
