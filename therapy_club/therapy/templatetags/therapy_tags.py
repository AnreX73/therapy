from django import template

from therapy.models import Graphics, ServiceCategory, Services

register = template.Library()


@register.inclusion_tag('therapy/components/header.html')
def header():
    logo = Graphics.objects.get(title='логотип')
    no_photo = Graphics.objects.get(title='нет фото')
    service_category = ServiceCategory.objects.exclude(title='Запасной порт')
   

    return {
        "logo": logo,
        'no_photo': no_photo,
        'service_category':service_category,
        
    }
