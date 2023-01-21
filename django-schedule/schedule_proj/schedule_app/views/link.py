from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Link
from schedule_app.serializers import LinkSerializer

@csrf_exempt
def link_list(request: HttpRequest):
    if request.method == 'GET':
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return JsonResponse(serializer.data, safe=False)