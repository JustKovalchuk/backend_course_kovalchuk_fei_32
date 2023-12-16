from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('random_course/', views.get_random_course_info, name="random_course"),
    path('get_course/', views.get_course_info, name="get_course"),
    path('get_course_sections/', views.get_course_sections, name="get_course_sections"),
    path("get_course_section_elements/", views.get_course_section_elements, name="get_course_section_elements"),
    path('all_courses/', views.get_all_courses_info, name="all_courses"),
    path('img/', views.get_all_courses_info, name="all_courses"),
]
