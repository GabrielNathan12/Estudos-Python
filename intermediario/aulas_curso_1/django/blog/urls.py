from django.contrib import admin
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog,name='home'),
    path('<int:_id>', views.post, name='post'), 

]
