from django.contrib import admin
from courses.models import CourseInfo


# Register your models here.
@admin.register(CourseInfo)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "rating", "image"]
