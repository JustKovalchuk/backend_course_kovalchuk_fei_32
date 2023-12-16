from django.contrib import admin
from courses.models import CourseInfo, Section, SectionElement


# Register your models here.
@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "rating", "image"]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "course"]


@admin.register(SectionElement)
class SectionElementAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "duration", "section"]
