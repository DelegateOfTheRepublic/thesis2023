from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import Department
from schedule_app.serializers import DepartmentSerializer

@csrf_exempt
def department_list(request: HttpRequest):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)