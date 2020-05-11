from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'date_of_birth', 'sex')}),
        (_('Permissions'), {'fields': ('is_active', 'is_professional', 'is_employer', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'photo', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'is_staff',
                    'is_professional', 'is_employer')
    list_filter = ('is_staff', 'is_professional', 'is_employer')
    search_fields = ('email', 'name',)
    ordering = ('email',)
