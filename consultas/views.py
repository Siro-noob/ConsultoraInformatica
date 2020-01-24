from django.shortcuts import render ,redirect
from .models import Tipo , Consulta


def home(request):
    return render(request,"consultas/home.html")

def index(request):
    return render(request,"consultas/index.html")

def contact(request):
    return render(request,"consultas/contact.html")



def home_admin(request):
    return render(request,"consultas_admin/home_admin.html")

def index_admin(request):
    return render(request,"consultas_admin/index_admin.html")

def contact_admin(request):
    return render(request,"consultas_admin/contact_admin.html")

