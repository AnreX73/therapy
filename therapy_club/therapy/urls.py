from django.urls import path

from therapy.views import index, rules, Coaches, service

urlpatterns = [
    path('', index, name='home'),
    path('rules/', rules, name='rules'),
    path('coach_list/', Coaches.as_view(), name='coaches'),
    path('service/<slug:slug>', service, name='service'),


]
