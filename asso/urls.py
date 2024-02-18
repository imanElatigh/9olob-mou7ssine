from django.urls import path
from asso import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('', views.login, name='login'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
      # Ensure this URL pattern is defined with the correct name
    # Add other URLs as needed
]
