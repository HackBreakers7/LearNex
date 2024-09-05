from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'standard',
                  'parent_name', 'contact_number', 'address', 'profile_image', 'school_name', 
                  'school_medium', 'educational_board', 'interests']
