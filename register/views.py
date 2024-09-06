from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        # Get user details from the form
        parent_first_name = request.POST.get('parent_first_name')
        parent_middle_name = request.POST.get('parent_middle_name')
        parent_last_name = request.POST.get('parent_last_name')
        parent_dob = request.POST.get('parent_dob')
        parent_gender = request.POST.get('parent_gender')
        parent_email = request.POST.get('parent_email')
        parent_contact_number = request.POST.get('parent_contact_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        child_first_name = request.POST.get('child_first_name')
        child_middle_name = request.POST.get('child_middle_name')
        child_last_name = request.POST.get('child_last_name')
        child_dob = request.POST.get('child_dob')
        child_gender = request.POST.get('child_gender')
        school_name = request.POST.get('school_name')
        school_medium = request.POST.get('school_medium')
        hobbies = request.POST.get('hobbies')
        address = request.POST.get('address')
        document_upload = request.FILES.get('document_upload')
        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match.'})

        # Create and save new user
        user = CustomUser(
            username=username,
            parent_first_name=parent_first_name,
            parent_middle_name=parent_middle_name,
            parent_last_name=parent_last_name,
            parent_dob=parent_dob,
            parent_gender=parent_gender,
            parent_email=parent_email,
            parent_contact_number=parent_contact_number,
            child_first_name=child_first_name,
            child_middle_name=child_middle_name,
            child_last_name=child_last_name,
            child_dob=child_dob,
            child_gender=child_gender,
            school_name=school_name,
            school_medium=school_medium,
            hobbies=hobbies,
            address=address,
            document_upload=document_upload,
            is_verified=False  # Automatically verified upon registration
        )
        user.set_password(password)  # Ensure the password is hashed
        user.save()
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_verified:
                auth_login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Your account is not verified yet. Please contact the admin.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.htm')
