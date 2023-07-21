from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Min, Max
import datetime
from request.models import Request
from django.db.models import Avg


@login_required(login_url='accounts:user_register')
def skills_add(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = SkillFrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            skill = Skills.objects.create(user=request.user, category=data['category'], title=data['title'],
                                          time=data['time'], description=data['description'])
            skill.save()
            messages.success(request, 'skill add')
        else:
            messages.error(request, 'enter valid data')
            print(form.errors)
    return redirect(url)


@login_required(login_url='accounts:user_register')
def skill_delete(request, id):
    skill = get_object_or_404(Skills, id=id)
    if skill.user == request.user:
        skill.delete()
        messages.success(request, 'deleted')
    return redirect('accounts:dashboard')


def skill_info(request, id):
    skill = get_object_or_404(Skills, id=id)
    avg = skill.rating.all().aggregate(Avg('rate'))
    info = skill.like.all()
    d1 = datetime.date.today()
    d2 = d1.month + 1
    if d2 < 10:
        d3 = f'0{d2}'
    else:
        d3 = d2
    context = {'skill': skill, 'next_month': d3, 'info': info,'avg':avg['rate__avg']}
    return render(request, 'skills/info.html', context)


def explore(request, slug=None):
    if slug:
        user = get_object_or_404(User, username=slug)
        if user.profile_user.complete:
            skills = Skills.objects.filter(user=user).order_by('-create')
        else:
            return redirect('home:main')
    else:
        skills = Skills.objects.all().order_by('-create')
    form = SearchForm()
    paginator = Paginator(skills, 12)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    contex = {'skills': page_obj, 'form': form}
    return render(request, 'skills/explore.html', contex)


def skill_search(request):
    skills = Skills.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            skills = skills.filter(Q(title__contains=data))
            paginator = Paginator(skills, 12)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)
    return render(request, 'skills/explore.html', {'form': form, 'skills': page_obj})


@login_required(login_url='accounts:user_register')
def skill_favorite(request, id):
    skill = get_object_or_404(Skills, id=id)
    if request.user == skill.user:
        return redirect('home:main')
    if request.user in skill.like.all():
        skill.like.remove(request.user)
        skill.save()
    else:
        skill.like.add(request.user)
        skill.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='accounts:user_register')
def skill_rate(request,id):
    rq = Request.objects.filter(id=id,user=request.user)
    if not rq.exists():
        return redirect('home:main')
    rq = Request.objects.get(id=id)
    skill = rq.skill
    if request.method == 'POST':
        form = SkillRateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['rate']
            rate = Rate.objects.create(rate=data)
            skill.rating.add(rate)
            skill.save()
            rq.delete()
            messages.success(request,'rated !')
        else:
            messages.error(request,'enter valid data')
    return redirect('request:all_request')
