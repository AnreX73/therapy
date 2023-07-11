from django.urls import path, include

from therapy.views import index, rules, Coaches

urlpatterns = [
    path('', index, name='home'),
    path('rules/', rules, name='rules'),
    path('coach_list/', Coaches.as_view(), name='coaches'),


]
