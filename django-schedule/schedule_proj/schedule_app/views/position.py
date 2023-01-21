from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Position
from schedule_app.serializers import PositionSerializer

@csrf_exempt
def position_list(request: HttpRequest):
    if request.method == 'GET':
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return JsonResponse(serializer.data, safe=False)