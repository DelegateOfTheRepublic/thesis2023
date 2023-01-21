from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import StudyFormat
from schedule_app.serializers import StudyFormatSerializer

@csrf_exempt
def study_format_list(request: HttpRequest):
    if request.method == 'GET':
        study_formats = StudyFormat.objects.all()
        serializer = StudyFormatSerializer(study_formats, many=True)
        return JsonResponse(serializer.data, safe=False)