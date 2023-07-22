from django.urls import include, path
from app import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('community/', views.community, name='community'),
    path('community/<int:content_id>/', views.content, name='content'),
    path('create/', views.create, name='create'),
    path('login/github/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
DEBUG = True