from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.main,name='main'),
    path('about',views.about,name='about'),
    path('send_mail/',views.send_mail,name='send_mail')
]