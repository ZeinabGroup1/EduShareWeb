from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.main,name='main'),
    path('contact/',views.contact_add,name='contact_add')
]
