from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^employees/<id>', views.EmployeeList.as_view()),
    url(r'^question/', views.QuestionList.as_view()),
    # url(r'^choice/', views.ChoiceList.as_view()),
    path(r'api/<question_id>/', views.QuestionRetrieveUpdateDelete.as_view()),
    path('', views.index),
    path('list/', views.viewquestionlist),

]