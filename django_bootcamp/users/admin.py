from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models

class UserAdmin(BaseUserAdmin):
    list_display = ('email', )
    search_fields = ('email', 'username', 'first_name', 'last_name')


admin.site.register(models.User, UserAdmin)