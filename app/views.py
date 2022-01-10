from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


# @login_required(login_url='/accounts/login/')
def index(request):
    hood = Neighbourhood.objects.all().order_by('-name')

    return render(request, 'all-temps/index.html')
