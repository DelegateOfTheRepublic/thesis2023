from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.urls import re_path
from schedule_app.models import Role
from schedule_app.serializers import RoleSerializer

@csrf_exempt
def role_list(request: HttpRequest):
    if request.method == 'GET':
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return JsonResponse(serializer.data, safe=False)


role_urls = [
    re_path(r'^roles/$', role_list)
]