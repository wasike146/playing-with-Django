from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage,name='main'),
    path('contacts/',views.reachUs,name='contacts')
]

