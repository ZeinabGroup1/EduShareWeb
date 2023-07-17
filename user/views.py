from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    if user.profile_user.complete:
        context = {'user': user}
        return render(request, 'user/user.html', context)
    else:
        return redirect('home:main')
