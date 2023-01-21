from turtle import position
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLevel
        fields = '__all__'

class StudyFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyFormat
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class StudyGroupSerializer(serializers.ModelSerializer):
    study_level = StudyLevelSerializer()
    course = CourseSerializer()

    class Meta:
        model = StudyGroup
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'

class DepartmentBoardSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Department
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()
    position = PositionSerializer()

    class Meta:
        model = Person
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    teacher = PersonSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Link
        fields = '__all__'

class StudyDaySerializer(serializers.ModelSerializer):
    study_group = StudyGroupSerializer()
    lesson = LessonSerializer()
    subject = SubjectSerializer()
    teacher = PersonSerializer()
    room = RoomSerializer()
    study_format = StudyFormatSerializer()

    class Meta:
        model = StudyDay
        fields = '__all__'