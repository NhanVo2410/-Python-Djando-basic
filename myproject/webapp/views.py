from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Employees, Question
from .serializers import EmployeesSerializers, QuestionSerializers


class EmployeeList(generics.ListCreateAPIView):
    employees = Employees.objects.all()
    serializer = EmployeesSerializers


# class themxoasua(generics.RetrieveUpdateDestroyAPIView):
#      lookup_field = 'emp_id'
#     serializer = EmployeesSerializers
#     employees = Employees.objects.all()


# Create your views here.

# employees = EmployeesSerializers(data=request.data)
# if serializer.is_valid():
#   serializer.save()
#   return Response(serializer.data, status=status.HTTP_201_CREATED)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializers
    queryset = Question.objects.all()

    ### different ways

    # def get(self, request):
    #     questions = Question.objects.all()
    #     serializer = QuestionSerializers(questions, many=True)
    #     return Response(serializer.data)
    #
    # # Create your views here.
    # def post(self):
    #     pass


class QuestionRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'question_id'
    serializer_class = QuestionSerializers
    queryset = Question.objects.all()


# class ChoiceList(APIView):
#
#     def get(self, request):
#         choice1 = Choice.objects.all()
#         serializer = ChoiceSerializers(choice1, many=True)
#         return Response(serializer.data)
#
#     # Create your views here.
#     def post(self):
#         fields = '__all__'

def index(request):
    return render(request, "home/index.html")


def viewquestionlist(request):
    # listquestion = get_object_or_404(Question,pk=3)
    listquestion = Question.objects.all()
    context = {"dsqt": listquestion}
    return render(request, "home/questionlist.html", context)
