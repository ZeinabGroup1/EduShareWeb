from django.shortcuts import render


def main(request):
    return render(request, 'home/main.html')


def about(request):
    return render(request, 'home/about.html')


def send_mail(request):
    pass