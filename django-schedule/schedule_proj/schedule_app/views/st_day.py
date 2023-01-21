from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import StudyDay
from schedule_app.serializers import StudyDaySerializer

@csrf_exempt
def study_day_list(request: HttpRequest):
    if request.method == 'GET':
        study_days = StudyDay.objects.all()
        serializer = StudyDaySerializer(study_days, many=True)
        return JsonResponse(serializer.data, safe=False)