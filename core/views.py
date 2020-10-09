from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Soy el Inicio")


def about(request):
    return HttpResponse("Soy la historia")


def services(request):
    return HttpResponse("Soy los servicios")


def store(request):
    return HttpResponse("Soy el visitanos")


def contact(request):
    return HttpResponse("Soy el contacto")


def blog(request):
    return HttpResponse("Soy el blog")


def sample(request):
    return HttpResponse("Soy el sample")
