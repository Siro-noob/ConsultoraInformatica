from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),

    path('index_admin/',views.index,name='index_admin'),
    path('home_admin/',views.home,name='home_admin'),
    path('contact_admin/',views.contact,name='contact_admin'),
]

