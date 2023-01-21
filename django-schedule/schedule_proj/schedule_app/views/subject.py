from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Subject
from schedule_app.serializers import SubjectSerializer

@csrf_exempt
def subject_list(request: HttpRequest):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)