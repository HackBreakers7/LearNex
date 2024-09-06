from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    parent_first_name = models.CharField(max_length=100,null=True)
    parent_middle_name = models.CharField(max_length=100, blank=True, null=True)
    parent_last_name = models.CharField(max_length=100,null=True)
    parent_dob = models.DateField(null=True)
    parent_gender = models.CharField(max_length=10,null=True)
    parent_email = models.EmailField(unique=True,null=True)
    parent_contact_number = models.CharField(max_length=15,null=True)
    child_first_name = models.CharField(max_length=100,null=True)
    child_middle_name = models.CharField(max_length=100, blank=True, null=True)
    child_last_name = models.CharField(max_length=100,null=True)
    child_dob = models.DateField(null=True)
    child_gender = models.CharField(max_length=10,null=True)
    school_name = models.CharField(max_length=200,null=True)
    school_medium = models.CharField(max_length=50,null=True)
    hobbies = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    document_upload = models.FileField(upload_to='documents/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
