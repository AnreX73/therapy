from django.urls import path, include

from therapy.views import index

urlpatterns = [
    path('', index, name='home'),


]
