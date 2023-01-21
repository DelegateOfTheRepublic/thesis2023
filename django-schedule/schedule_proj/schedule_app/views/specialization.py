from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Specialization
from schedule_app.serializers import SpecializationSerializer

@csrf_exempt
def specializations_list(request: HttpRequest):
    if request.method == 'GET':
        specializations = Specialization.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return JsonResponse(serializer.data, safe=False)