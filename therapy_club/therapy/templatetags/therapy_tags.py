from django import template

from therapy.models import Graphics

register = template.Library()


@register.inclusion_tag('therapy/components/header.html')
def header():
    logo = Graphics.objects.get(title='логотип')
    no_photo = Graphics.objects.get(title='нет фото')

    return {
        "logo": logo,
        'no_photo': no_photo,

    }
