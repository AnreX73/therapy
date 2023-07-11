from django import template

from therapy.models import Graphics, ServiceCategory, Services

register = template.Library()


@register.inclusion_tag('therapy/components/header.html')
def header():
    logo = Graphics.objects.get(title='логотип')
    no_photo = Graphics.objects.get(title='нет фото')
    service_category = ServiceCategory.objects.exclude(title='Запасной порт')
    main_image = Graphics.objects.get(title='картинка на главную')
   

    return {
        "logo": logo,
        'no_photo': no_photo,
        'service_category':service_category,
        'main_image':main_image
        
    }
