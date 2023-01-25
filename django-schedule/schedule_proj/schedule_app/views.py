from typing import List
from django.http import HttpResponse, JsonResponse, HttpRequest, QueryDict
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import *
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import *
from .services import *

# Create your views here.
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return JsonResponse(status=status.HTTP_200_OK)

class CourseApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = CourseSerializer(SCourse.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class DepartmentApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = DepartmentSerializer(SDepartment.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class DepartmentBoardApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = DepartmentBoardSerializer(SDepartmentBoard.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class LessonApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = LessonSerializer(SLesson.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class LinkApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = LinkSerializer(SLink.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class PositionApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = PositionSerializer(SPosition.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class PersonApi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request) -> JsonResponse:
        #the code below is temporary
        
        persons = SPerson.get_all()
        teacher_serializer: List[QueryDict] = []
        another_serializer: List[QueryDict] = []

        if persons.get('teachers', None):
            teacher_serializer = TeacherSerializer(persons.get('teachers'), many=True).data

        if persons.get('anothers', None):
            another_serializer = PersonSerializer(persons.get('anothers'), many=True).data

        if request.GET.get('id'):
            person = SPerson.get_person_by_id(request.GET.get('id'))
            if person.role == 'Преподаватель':
                return JsonResponse(TeacherSerializer(person).data, safe=False)
            return JsonResponse(PersonSerializer(person).data, safe=False)
        
        serializer = teacher_serializer + another_serializer
        return JsonResponse(serializer, safe=False)

    def post(self, request, format=None) -> JsonResponse:
        parser_classes = [MultiPartParser, FormParser]
        role = request.data.get('role', None)
        print(request.data)

        if role == '2':
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                print('val_data ', serializer.validated_data)
                SPerson.create_teacher(serializer.validated_data)
                return JsonResponse({'success': 'teacher created'})
        else:
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid():
                SPerson.create_person(serializer.validated_data)
                return JsonResponse({'success': 'person created'})
        
        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request, format=None):
        parser_classes = [MultiPartParser, FormParser]

        serializer = PersonSerializer(SPerson.get_person_by_id(request.query_params.get('id', None)), data=request.data, partial=True)
        if serializer.is_valid():
            SPerson.update_person(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status':status.HTTP_400_BAD_REQUEST})

class RoleApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = RoleSerializer(SRole.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class RoomTypeApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = RoomTypeSerializer(SRoomType.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class RoomApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = RoomSerializer(SRoom.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyLevelApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = StudyLevelSerializer(SStudyLevel.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyGroupApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = StudyGroupSerializer(SStudyGroup.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyFormatApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = StudyFormatSerializer(SStudyFormat.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyDayApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = StudyDaySerializer(SStudyDay.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request) -> JsonResponse:
        data = request.data
        if isinstance(data, dict):
            data = [data]

        serializer = StudyDaySerializer(data=data, many=True)

        if serializer.is_valid():
            SStudyDay.create_study_days(serializer.validated_data)
            return JsonResponse({'success': 'study days created'})
        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

class SubjectApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = SubjectSerializer(SSubject.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class SpecializationApi(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        serializer = SpecializationSerializer(SSpecialization.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class UploadScheduleTemplatesApi(APIView):
    def post(self, request) -> JsonResponse:
        parser_classes = [MultiPartParser, FormParser]
        print(request.data)
        templates = request.data.get('templates', None)

        if templates and len(templates) != 0:
            print(templates)
            return JsonResponse({'success': 'templates created'})
            
        return JsonResponse({'KeyError': 'request data must have `templates` key'})