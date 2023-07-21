"""
URL configuration for skill_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Login to Skill Hub";
admin.site.site_title =  " Welcome to Skill's Hub Dashboard";
admin.site.site_index =  " Welcome to the Portal ";


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('account.urls',namespace='accounts')),
    path('',include('home.urls',namespace='urls')),
    path('blog/', include('blog.urls', namespace='blog')),  # Include the blog app URLs with a namespace
    path('skills/',include('skills.urls',namespace='skills')),
    path('user/',include('user.urls',namespace='user')),
    path('request/',include('request.urls',namespace='request')),
    path('auth/', include('social_django.urls', namespace='social')),#For Social Django Authentication
    path('', include('admin_material.urls')),# Admin panel
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
