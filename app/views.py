from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


# @login_required(login_url='/accounts/login/')
def index(request):
    hood = Neighbourhood.objects.all().order_by('-name')
    return render(request, 'all-temps/index.html')


def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    hood = Neighbourhood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    posts = Post.objects.filter(user_id=current_user.id)
    return render(request, "all-temps/profile.html", {"profile": profile, 'hood': hood, 'businesses': businesses, "posts": posts, })


def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    return render(request, 'all-temps/update_prof.html', {"form": form}, ctx)


@login_required(login_url='/accounts/login/')
def create_business(request):
    current_user = request.user
    if request.method == "POST":

        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.hood = hood
            business.save()
        return HttpResponseRedirect('/busineses')
    else:
        form = BusinessForm()
    return render(request, 'all-temps/create-business.html', {'form': form, 'profile': profile})


@login_required(login_url="/accounts/login/")
def busineses(request):
    current_user = request.user
    busineses = Business.objects.all().order_by('-id')

    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()

        locations = Location.objects.all()
        hood = Neighbourhood.objects.all()

        busineses = Business.objects.all().order_by('-name')

        return render(request, "all-temps/profile.html", {"danger": "Update Profile", "locations": locations, "hood": hood, "busineses": busineses})
    else:
        neighborhood = profile.neighborhood
        busineses = Business.objects.all().order_by('-id')
        return render(request, "all-temps/business.html", {"busineses": busineses})
