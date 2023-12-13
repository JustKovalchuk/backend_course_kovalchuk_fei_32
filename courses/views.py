from django.http import HttpResponse, HttpRequest
from .models import CourseInfo
import random
from django.core.serializers import serialize


def get_random_course_info(request: HttpRequest):
    all_objects = CourseInfo.objects.all()

    if all_objects.exists():
        random_element = random.choice(all_objects)
        serialized_element = serialize('json', [random_element])

        return HttpResponse(serialized_element, content_type='application/json')
    else:
        return HttpResponse("NONE")


def get_course_info(request: HttpRequest):
    all_objects = CourseInfo.objects.all()

    for obj in all_objects:
        if request.POST["id"] == obj["url_text"]:
            serialized_element = serialize('json', obj)
            return HttpResponse(serialized_element)

    return HttpResponse("NONE")


def get_all_courses_info(request: HttpRequest):
    all_objects = CourseInfo.objects.all()

    if all_objects.exists():
        serialized_element = serialize('json', all_objects)

        return HttpResponse(serialized_element, content_type='application/json')
    else:
        serialized_element = serialize('json', [])
        return HttpResponse(serialized_element)
