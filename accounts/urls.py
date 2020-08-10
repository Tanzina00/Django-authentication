from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', include('material.admin.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),  name='home')
]
