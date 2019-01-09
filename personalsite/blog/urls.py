from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me', views.about_me, name='about-me'),
    path('blog', views.blog, name='blog'),
    path('curriculum', views.curriculum, name='curriculum'),
    path('contact', views.contact, name='contact'),
]
