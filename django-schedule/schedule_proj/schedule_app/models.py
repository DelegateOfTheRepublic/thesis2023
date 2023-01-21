from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class StudyLevel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class StudyFormat(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    number = models.IntegerField(max_length=1)

    def __str__(self) -> str:
        return f'{self.number} курс'

class StudyGroup(models.Model):
    name = models.CharField(max_length=128)
    study_level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.short_name

class RoomType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.number

class DepartmentBoard(models.Model):
    name = models.CharField(max_length=256)
    number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

def create_user_data_path(person, filename: str) -> str:
    return f'users_data/{person.user.email}/{filename}'

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to=create_user_data_path)
    show_conts = models.CharField(max_length=16, default='1, 1')
    from_another_uni = models.BooleanField(default=False)
    teacher_schedule = models.FileField(upload_to=create_user_data_path, validators=[FileExtensionValidator(allowed_extensions=["json"])])
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.middle_name}'

class Link(models.Model):
    platform_name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='platform_icons/')
    meeting_ident = models.CharField(max_length=32, blank=True, null=True)
    passcode = models.CharField(max_length=16, blank=True, null=True)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.platform_name

class Lesson(models.Model):
    ordinal_number = models.IntegerField(max_length=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return f'{self.ordinal_number} пара'

class StudyDay(models.Model):
    DAY_NUMBERS = [
        ("0", "Понедельник"),
        ("1", "Вторник"),
        ("2", "Среда"),
        ("3", "Четверг"),
        ("4", "Пятница"),
        ("5", "Суббота")
    ]

    day_number = models.CharField(choices=DAY_NUMBERS, max_length=1)
    is_fractional = models.BooleanField(default=False)
    is_top_week = models.BooleanField(default=False)
    actual_dates = models.CharField(max_length=256, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    study_format = models.ForeignKey(StudyFormat, on_delete=models.CASCADE)
    links = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self) -> str:
        return self.day_number