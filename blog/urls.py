
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.main, name='main'),
    # Add other URL patterns as needed
    path('detail/<int:blog_id>/',views.detail,name='detail'),

]
