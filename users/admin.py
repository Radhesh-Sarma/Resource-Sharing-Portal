from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,userdata
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','mobile_number','address']
    fieldsets = (
        (('User'), {'fields': ('username', 'email','is_staff', 'mobile_number','address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(userdata)