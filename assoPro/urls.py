"""assoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from asso import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', views.sign_up, name='sign-up'),  # URL for sign-up view
    path('login/', views.login, name='login'),  # URL for login view
    path('',include('asso.urls')),
    # path('', login_required(views.home_view), name='home'),
    path('profile/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
    # Add more URLs for other views if needed
]