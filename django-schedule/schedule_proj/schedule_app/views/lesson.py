from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Lesson
from schedule_app.serializers import LessonSerializer

@csrf_exempt
def lesson_list(request: HttpRequest):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return JsonResponse(serializer.data, safe=False)