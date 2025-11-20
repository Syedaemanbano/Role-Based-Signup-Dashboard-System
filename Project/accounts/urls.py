# accounts/urls.py

from django.urls import path
from . import views

# CRITICAL: Define the app_name for the namespace
app_name = 'accounts'
urlpatterns = [
    # Core Objectives
    path('', views.login_view, name='login'), # 2. Login Logic (Root URL)
    path('signup/', views.signup_view, name='signup'), # 1. Signup Page
    path('logout/', views.user_logout, name='logout'),
    
    # 4. Dashboard Interfaces
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    
    # Extra Marks: CRUD Operations
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'), # 5. Delete
    path('user/update/<int:user_id>/', views.update_user, name='update_user'), # 6. Update
]