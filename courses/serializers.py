from rest_framework import serializers
from .models import Section, SectionElement, CourseInfo


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SectionElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionElement
        fields = '__all__'
