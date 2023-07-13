from django.urls import path
from . import views

app_name = 'request'

urlpatterns = [
    path('',views.all_request,name='all_request'),
    path('add/<int:id>/',views.request_add,name='request_add'),
    path('<int:id>/',views.request_details,name='request_details'),
    path('accept/<int:id>/',views.request_accept,name='request_accept'),
    path('reject/<int:id>/',views.request_reject,name='reject'),
]