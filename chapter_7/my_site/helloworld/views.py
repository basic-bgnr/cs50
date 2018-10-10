from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime

from django.core.exceptions import ObjectDoesNotExist
from .models import TimeDatabase

# Create your views here.
def index(request):
    context = {
            'cities': TimeDatabase.objects.all(),
            }
    return render(request=request, template_name='index.html', context=context)


def timepages(request, timepagesnum):
    try:
        data = TimeDatabase.objects.get(pk=timepagesnum)
    except ObjectDoesNotExist:
        return Http404("Flights not found")
    context = {
            'cities': [data]
            }
    return render(request=request, template_name='index.html', context=context) 
