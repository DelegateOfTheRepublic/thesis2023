from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import StudyGroup
from schedule_app.serializers import StudyGroupSerializer

@csrf_exempt
def study_group_list(request: HttpRequest):
    if request.method == 'GET':
        study_groups = StudyGroup.objects.all()
        serializer = StudyGroupSerializer(study_groups, many=True)
        return JsonResponse(serializer.data, safe=False)