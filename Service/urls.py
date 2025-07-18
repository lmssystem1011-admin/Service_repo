"""
URL configuration for Service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('',home,name='home'),
    path('admin_dash/',admin_panel,name="admin_panel"),
    path('add_college/',add_college,name="add_college"),
    path('admin_profile/',admin_profile, name="admin_profile"),
    path('update_admin_profile/',update_admin_profile,name='update_admin_profile'),
    path('college_master/',college_master,name="college_master"),
    path('userlogout/',userlogout,name="logout"),
    path('add_subject/',add_subject,name="add_subject"),
    path('subject_master/',subject_master,name="subject_master"),
    path('get_universities/',get_universities,name="get_universities"),
    path('get_branches/', get_branches, name='get_branches'),
]
