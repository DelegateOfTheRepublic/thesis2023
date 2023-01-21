from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from schedule_app.models import DepartmentBoard
from schedule_app.serializers import DepartmentBoardSerializer

@csrf_exempt
def department_board_list(request: HttpRequest):
    if request.method == 'GET':
        department_boards = DepartmentBoard.objects.all()
        serializer = DepartmentBoardSerializer(department_boards, many=True)
        return JsonResponse(serializer.data, safe=False)