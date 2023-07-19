from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from skills.models import Skills


def main(request):
    all_skills = Skills.objects.all()[:3]
    context = {'all_skills':all_skills}
    return render(request, 'home/main.html',context)


def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Contact.objects.create(name=data['name'], email=data['email'], text=data['text'])
            messages.success(request, 'your form added')
            return redirect('home:main')
        else:
            messages.error(request, 'enter valid data')
