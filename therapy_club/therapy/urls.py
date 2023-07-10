from django.urls import path, include

from therapy.views import index,rules

urlpatterns = [
    path('', index, name='home'),
    path('/rules', rules, name='rules'),


]
