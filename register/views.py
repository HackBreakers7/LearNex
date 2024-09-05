from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


# Create your views here.
def index (request):
    return render(request,'index.htm')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after successful registration
            return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the name of the view you want to redirect to
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

