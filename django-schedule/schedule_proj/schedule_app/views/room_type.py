from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import RoomType
from schedule_app.serializers import RoomTypeSerializer

@csrf_exempt
def room_type_list(request: HttpRequest):
    if request.method == 'GET':
        room_types = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_types, many=True)
        return JsonResponse(serializer.data, safe=False)