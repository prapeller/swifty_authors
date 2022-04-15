from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ("pkid",)
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("pkid", "id", "email", "username", "first_name", "last_name", "is_staff", "is_active")
    list_display_links = ("id", "email")
    list_filter = ("email", "username", "first_name", "last_name", "is_staff")
    fieldsets = (
        (_("Credentials"), {"fields": ("email", "password")}),
        (_("Personal information"), {"fields": ("first_name", "last_name")}),
        (_("Status"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Permissions"), {"fields": ("groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("date_joined", "last_login")}),
    )
    add_fieldsets = (
        (_('Credentials'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        (_('Status'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    search_fields = ("email", "username", "first_name", "last_name")


admin.site.register(User, UserAdmin)
