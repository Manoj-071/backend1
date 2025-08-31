"""
URL configuration for mainproject project.

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
from tracker import views  # Import views from the tracker app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view, name='login'),  # Login view
    path('register/', views.register_view, name='register'),  # Registration view
    path('addproblem/', views.addproblem_view, name='addproblem'),  # Add problem view
    path('tags/', views.tags_view, name='tags'),  # Tags view
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard view
    path('user_activity/', views.user_activity_view, name='user_activity'),  # User activity view
    path('mquotes/', views.mquotes_view, name='mquotes'),  # Motivational quotes view
]
