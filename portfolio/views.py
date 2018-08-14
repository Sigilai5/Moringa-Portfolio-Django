from django.shortcuts import render
from .models import Projects
from django.http import HttpResponse,Http404


# Create your views here.
def home(request):
    images = Projects.objects.all()

    return render (request,'home.html',locals())
