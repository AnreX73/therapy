from django.urls import path, include

from django.conf.urls.static import static

from therapy.views import index
from therapy_club import settings

urlpatterns = [
    path('', index, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
