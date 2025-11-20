from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import CustomUser

# Helper for Redirection Logic
def redirect_by_role(user):
    """Helper function to redirect based on user role after successful login."""
    if user.is_admin:
        return redirect('accounts:admin_dashboard')
    elif user.is_customer:
        return redirect('accounts:customer_dashboard')
    return redirect('accounts:login')  # FIXED


# Helper for Security Check (Admin access)
def is_admin_check(user):
    """Checks if the user is authenticated and has the 'ADMIN' role."""
    return user.is_authenticated and user.is_admin


# --- 1. Signup Page (/signup/) ---
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful. Please log in.')
            return redirect('accounts:login')    # FIXED
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


# --- 2. Login Logic (/)
def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # Debug: Check user role before redirect
                print(f"DEBUG: User {user.username} logged in with role: {user.role}")
                print(f"DEBUG: is_customer: {user.is_customer}, is_admin: {user.is_admin}")
                redirect_response = redirect_by_role(user)
                print(f"DEBUG: Redirecting to: {redirect_response.url}")
                return redirect_response
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            # Form validation failed
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# --- Logout View ---
@login_required
def user_logout(request):
    """Logout the user and redirect to login page."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:login')


# --- 4. Dashboard Interfaces ---

# Customer Dashboard
@login_required
def customer_dashboard(request):
    """Customer dashboard - displays user's username and email."""
    # Security: Only customers can access this dashboard
    if not request.user.is_customer:
        messages.error(request, 'Access denied. You do not have permission to view this page.')
        return redirect_by_role(request.user)
    
    return render(request, 'accounts/customer_dashboard.html', {
        'user': request.user
    })


# Admin Dashboard
@login_required
@user_passes_test(is_admin_check, login_url='/')
def admin_dashboard(request):
    """Admin dashboard - displays all registered users in a table."""
    all_users = CustomUser.objects.all().order_by('id')
    return render(request, 'accounts/admin_dashboard.html', {
        'all_users': all_users
    })


# --- Extra Marks: CRUD Operations ---

# Delete User Functionality
@login_required
@user_passes_test(is_admin_check, login_url='/')
def delete_user(request, user_id):
    """Delete a user from the database. Only admins can perform this action."""
    if request.method == 'POST':
        user_to_delete = get_object_or_404(CustomUser, id=user_id)
        
        # Prevent admin from deleting themselves
        if user_to_delete == request.user:
            messages.error(request, 'You cannot delete your own account.')
            return redirect('accounts:admin_dashboard')
        
        username = user_to_delete.username
        user_to_delete.delete()
        messages.success(request, f'User "{username}" has been deleted successfully.')
        return redirect('accounts:admin_dashboard')
    
    # If not POST, redirect to admin dashboard
    return redirect('accounts:admin_dashboard')


# Update User Functionality
@login_required
@user_passes_test(is_admin_check, login_url='/')
def update_user(request, user_id):
    """Update a user's information. Only admins can perform this action."""
    target_user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=target_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User "{target_user.username}" has been updated successfully.')
            return redirect('accounts:admin_dashboard')
    else:
        form = UserUpdateForm(instance=target_user)
    
    return render(request, 'accounts/update_user.html', {
        'form': form,
        'target_user': target_user
    })
