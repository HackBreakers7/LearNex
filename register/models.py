from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    standard = models.CharField(max_length=10, blank=True)
    parent_name = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    school_medium = models.CharField(max_length=50, blank=True)
    educational_board = models.CharField(max_length=50, blank=True)
    interests = models.TextField(blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changed related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set_permissions',  # Changed related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    def __str__(self):
        return self.username
