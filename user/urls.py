from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('<username>/',views.user_profile,name='user_profile')
]