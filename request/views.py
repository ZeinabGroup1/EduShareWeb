from django.shortcuts import render, get_object_or_404, redirect
from .forms import RequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Messages
from django.db.models import Q
from skills.models import Skills
from .models import Request

@login_required(login_url='accounts:user_register')
def request_add(request, id):
    skill = get_object_or_404(Skills, id=id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Request.objects.filter(receiver=skill.user, date=data['date'], time=data['time']):
                messages.warning(request, 'User time slot is full')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                request_obj = Request.objects.create(skill=skill, user=request.user, receiver=skill.user, status='pending',
                                       date=data['date'], time=data['time'])
                messages.success(request, 'Request added')
                # Send a message to the receiver
                Messages.objects.create(sender=request.user, receiver=skill.user, content=f'You have a new request for skill {skill.title}.')
        else:
            messages.error(request, 'Enter valid date')
    return redirect('home:main')

@login_required(login_url='accounts:user_register')
def all_request(request):
    # Retrieve requests where the user is either the receiver or the sender and the status is accepted
    requests = Request.objects.filter(Q(receiver=request.user) | Q(user=request.user, status='accepted')).order_by('-create')
    context = {'requests': requests}
    return render(request, 'request/request.html', context)

@login_required(login_url='accounts:user_register')
def request_details(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver != request.user:
        return redirect('home:main')
    requests = Request.objects.filter(Q(receiver=request.user) | Q(user=request.user, status='accepted')).order_by('-create')
    context = {'requests': requests, 'rq': rq}
    return render(request, 'request/details.html', context)

@login_required(login_url='accounts:user_register')
def request_accept(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver != request.user:
        return redirect('home:main')
    rq.status = 'accepted'
    rq.save()
    messages.success(request, 'Request accepted')
    # Send a message to the sender
    Messages.objects.create(sender=request.user, receiver=rq.user, content=f'Your request for skill {rq.skill.title} has been accepted.')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='accounts:user_register')
def request_reject(request, id):
    rq = get_object_or_404(Request, id=id)
    if rq.receiver == request.user or (rq.user == request.user and rq.status == 'accepted'):
        rq.delete()
        messages.success(request, 'Request deleted')
        Messages.objects.create(sender=request.user, receiver=rq.user, content=f'Your request for skill {rq.skill.title} has been rejected / deleted.')
        Messages.objects.create(sender=request.user, receiver=rq.receiver, content=f'The request for your skill {rq.skill.title} has been canceled / deleted.')
    return redirect('request:all_request')
