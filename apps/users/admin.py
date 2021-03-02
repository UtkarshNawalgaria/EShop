from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomerModel, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomerModel)
class CustomerAdmin(ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_customer',)
    list_filter = ('email', 'is_customer',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ("Seller/Customer", {'fields': ('is_customer',)}),
        ("Permissions", {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ("Login Details", {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_customer',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
