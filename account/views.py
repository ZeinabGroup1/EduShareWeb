from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from skills.models import *

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['user_name'], email=data['email'], password=data['password'])
            user.active = True
            user.save()
            messages.success(request, 'welcome')
            return redirect('home:main')
        else:
            messages.error(request, 'enter valid data')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you loged in')
                return redirect('home:main')
            else:
                messages.warning(request, 'wrong information')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/register.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'you have loged out')
    return redirect('home:main')


@login_required(login_url='accounts:user_register')
def dashboard(reuqest):
    user = User.objects.get(id=reuqest.user.id)
    all_category = SkillsCategory.objects.all()
    all_times = SkillsTime.objects.all()
    user_skills = Skills.objects.filter(user=reuqest.user)
    context = {'user': user,'all_category':all_category,'all_times':all_times,'user_skills':user_skills}
    return render(reuqest, 'accounts/dashboard.html', context)


@login_required(login_url='accounts:user_register')
def user_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile_user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'updated')
        else:
            messages.error(request, 'enter valid data')
            print(profile_form.errors)
    else:
        profile_form = ProfileForm(instance=request.user.profile_user)
    context = {'profile_form': profile_form}
    return render(request, 'accounts/profile.html', context)
