from django.contrib import admin
from .models import CustomUser, OTP

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'parent_email', 'is_verified')
    search_fields = ('username', 'parent_email')

class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'is_verified', 'created_at')
    search_fields = ('user__username', 'otp_code')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTP, OTPAdmin)
