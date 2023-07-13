from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Messages
from django.db.models import Q


@login_required(login_url='accounts:user_register')
def request_add(request, id):
    skill = get_object_or_404(Skills, id=id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Request.objects.filter(receiver=skill.user, date=data['date'], time=data['time']):
                messages.warning(request, 'user Time is full')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                Request.objects.create(skill=skill, user=request.user, receiver=skill.user, status='pending',
                                       date=data['date'], time=data['time'])
                messages.success(request, 'request added')
        else:
            messages.error(request, 'enter valid date')
    return redirect('home:main')


@login_required(login_url='accounts:user_register')
def all_request(request):
    requests = Request.objects.filter(receiver=request.user).order_by('-create')
    requests = Request.objects.filter(Q(receiver=request.user) | Q(user=request.user) & Q(status='accepted')).order_by(
        '-create')
    context = {'requests': requests}
    return render(request, 'request/request.html', context)


@login_required(login_url='accounts:user_register')
def request_details(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver != request.user:
        redirect('home:main')
    requests = Request.objects.filter(Q(receiver=request.user) | Q(user=request.user) & Q(status='accepted')).order_by(
        '-create')
    context = {'requests': requests, 'rq': rq}
    return render(request, 'request/details.html', context)


@login_required(login_url='accounts:user_register')
def request_accept(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver != request.user:
        redirect('home:main')
    rq.status = 'accepted'
    rq.save()
    messages.success(request, 'request accepted')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='accounts:user_register')
def request_reject(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver == request.user or rq.user == request.user and rq.status == 'accepted':
        rq.delete()
        messages.success(request, 'request deleted')
        Messages.objects.create(user=rq.user, text=f'your request for skill {rq.skill.id} rejected / deleted')
        Messages.objects.create(user=rq.receiver, text=f'the request for your skill {rq.skill.id} canceled / deleted')
        return redirect('request:all_request')
    else:
        redirect('home:main')
