from django.shortcuts import render
from django.views.generic import ListView

from therapy.models import Services, Graphics, Coaches, Post, ServiceCategory, Gallery, Contacts


def index(request):
    services = Services.objects.exclude(title='х-запасной порт')
    service_cats = ServiceCategory.objects.exclude(title='Запасной порт').order_by('-pk')
    cats_images = Gallery.objects.exclude(gallery_link_id=6).select_related('gallery_link')
    contacts = Contacts.objects.exclude(title='Карта')
    contacts_map = Contacts.objects.get(title='Карта')

    context = {
        'title': 'Главная страница',
        'services': services,
        'service_cats': service_cats,
        'cats_images': cats_images,
        'contacts': contacts,
        'contacts_map':contacts_map

    }

    return render(request, 'therapy/index.html', context=context)


def rules(request):
    rules = Post.objects.get(title='Правила посещения')
    context = {
        'rules': rules
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
