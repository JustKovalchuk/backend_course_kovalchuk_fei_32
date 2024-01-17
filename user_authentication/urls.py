from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name="home"),
    path('add_course_to_user/', views.add_course_to_user, name="add_course_to_user")
]
