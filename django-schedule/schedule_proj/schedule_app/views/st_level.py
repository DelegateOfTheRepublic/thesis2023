from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import StudyLevel
from schedule_app.serializers import StudyLevelSerializer

@csrf_exempt
def study_level_list(request: HttpRequest):
    if request.method == 'GET':
        study_levels = StudyLevel.objects.all()
        serializer = StudyLevelSerializer(study_levels, many=True)
        return JsonResponse(serializer.data, safe=False)