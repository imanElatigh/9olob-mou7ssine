from django.urls import path
from asso import views
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create_post, name='create_post'),
    path('', views.index, name='index'),
    path('search/', views.search_response, name='search_response'),
    path('association/<int:association_id>/', views.association_detail, name='association_detail'),
    path('association_user/<int:user_id>/', views.association_user_detail, name='association_user_detail'),
    # Ensure this URL pattern is defined with the correct name
    # Add other URLs as needed
]
