from django.http import HttpResponse, HttpRequest
from .models import CourseInfo, Section, SectionElement
import random
from django.core.serializers import serialize
import json
from .serializers import SectionElementSerializer, SectionSerializer


def get_random_course_info(request: HttpRequest):
    all_objects = CourseInfo.objects.all()

    if all_objects.exists():
        random_element = random.choice(all_objects)
        serialized_element = serialize('json', [random_element])

        return HttpResponse(serialized_element, content_type='application/json')
    else:
        return HttpResponse("NONE")


def get_course_info(request: HttpRequest):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        obj = CourseInfo.objects.get(url_text=body["id"])
        serialized_element = serialize('json', [obj])
        return HttpResponse(serialized_element)
    return HttpResponse("NONE")


def get_course_sections(request: HttpRequest):
    combined = {
        "sections": [],
        "elements": []
    }
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        course_obj = CourseInfo.objects.get(url_text=body["id"])
        sections_obj = Section.objects.filter(course=course_obj).order_by('order')
        section_serializer = SectionSerializer(sections_obj, many=True)
        section_elements = SectionElement.objects.filter(section__in=sections_obj).order_by('order')
        section_element_serializer = SectionElementSerializer(section_elements, many=True)

        sec_dic = {}
        for sec in section_serializer.data:
            sec_dic.update({sec['id']: []})
        for sec_el in section_element_serializer.data:
            sec_dic.get(sec_el['section']).append(sec_el)

        combined = {
            "sections": section_serializer.data,
            "elements": sec_dic
        }

    return HttpResponse(json.dumps(combined))


def get_course_section_elements(request: HttpRequest):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        section_obj = Section.objects.get(id=body["sectionId"])
        # section_serializer = SectionSerializer(section_obj, many=True)
        # print("section_obj", section_obj)
        section_elements = SectionElement.objects.filter(section=section_obj).order_by('order')
        # section_element_serializer = SectionElementSerializer(section_elements, many=True)
        # # print("section_elements", section_elements)
        # combined_data = {
        #     'authors': section_serializer.data,
        #     'books': section_element_serializer.data,
        # }
        #
        # print("result", combined_data)

        serialized_element = serialize('json', section_elements)
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
