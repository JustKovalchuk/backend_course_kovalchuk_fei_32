from django.contrib import admin
from user_authentication.models import UserAccount


# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["email", "password", "first_name", "last_name", "is_active", "is_staff"]
