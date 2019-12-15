from rest_framework import serializers
from .models import Employees, Question


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['username', 'password', 'emp_id']


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'time']


# class AdminSerializer(serializers.ModelSerializer):
#     creater_name = QuestionSerializers(read_only=True, many=True)
#
#     class Meta:
#         model = Admin
#         fields = '__all__'

# class ChoiceSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Choice
#         fields = ['choice_text', 'vote']
