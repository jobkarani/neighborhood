from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


def index(request):

    return render(request, 'all-temps/index.html')
