from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Praca, Skills, Hobby


# Create your views here.
def home(request):
    return render(request, 'home.html')


def kontakt(request):
    return render(request, 'kontakt.html')


def doswiadczenie(request):
    prace = Praca.objects.all()
    return render(request, 'doswiadczenie.html', {'prace': prace})


def hobby(request):
    hobbys = Hobby.objects.all()
    return render(request, 'hobby.html', {'hobbys': hobbys})


def umiejetnosci(request):
    skills = Skills.objects.all()
    return render(request, 'umiejetnosci.html', {'skills': skills})


def strona_glowna(request):
    return redirect('/')
