from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('about/', views.about, name='about'),
    path('about/about.html/', views.about, name='about'),
    path('admin/', admin.site.urls)
]
