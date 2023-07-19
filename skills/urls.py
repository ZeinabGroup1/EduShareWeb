from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('add/', views.skills_add, name='skills_add'),
    path('delete/<int:id>/', views.skill_delete, name='skill_delete'),
    path('<int:id>/', views.skill_info, name='skill_info'),
    path('explore/', views.explore, name='explore'),
    path('explore/<slug>/', views.explore, name='user_explore'),
    path('search/', views.skill_search, name='skill_search'),
]
