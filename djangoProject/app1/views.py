# app1/views.py

from django.shortcuts import render, redirect
from app1.models import WriteSomething
from app1.forms import WriteSomethingForm

def community(request):
    data_list = WriteSomething.objects.all()
    return render(request, "community.html", {"data_list": data_list})


def create(request):
    if request.method == 'POST':
        form = WriteSomethingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = WriteSomethingForm()

    return render(request, 'create.html', {'form': form})

