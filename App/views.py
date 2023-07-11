import requests
from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError
from requests.exceptions import ConnectionError
from App.config import github_profile


def login(request):
    try:
        login_type = request.GET['type']

    except MultiValueDictKeyError:
        return render(request, 'login.html')

    if login_type == 'github':
        code = request.GET['code']

        try:
            response_code = requests.post(
                f'https://github.com/login/oauth/access_token?client_id={github_profile["client_id"]}&client_secret={github_profile["client_secret"]}&code={code}')

            response_info = requests.get('https://api.github.com/user', headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": "token " + response_code.text.split('&')[0].split('=')[1]
            })

        except ConnectionError:
            return redirect('/timeout')

        print('Username:', response_info.json()['login'], 'UserID:', response_info.json()['id'])
        return redirect('/home')


def timeout(request):
    return HttpResponse('TimeOut')


def home(request):
    return HttpResponse('Hello')
