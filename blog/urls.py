from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('newpic/', views.picpost, name='newpic'),
    path('upload/', views.uploadfileform, name='upload'),
]