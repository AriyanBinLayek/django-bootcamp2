from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Profile', 
         {
            'fields': (
                'shipping_first_name', 'shipping_last_name', 'shipping_country',
                'shipping_state', 'shipping_city', 'shipping_street',
                'shipping_zip', 'shipping_phone'
            )
         }
        ),
    )
    

admin.site.register(models.User, UserAdmin)