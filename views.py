from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView


def update_profile(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('your_app_name:dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile/update.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
