from django.http import HttpResponse, HttpRequest
from django.core.serializers import serialize
from .models import UserAccount

import json

def home(request: HttpRequest):
    return HttpResponse("authentication page")


def add_course_to_user(request: HttpRequest):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = UserAccount.objects.filter(id=body["id"])
    serialized_element = serialize('json', user)
    print(user)
    return HttpResponse("NONE")
