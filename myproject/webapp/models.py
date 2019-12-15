from django.db import models
# from myproject.user.models import Admin
# Create your models here.
class Employees(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.username


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)

    # creater_name = models.ManyToManyField(Admin, related_name='creater_name')
    time = models.DateTimeField()

    def __str__(self):
        return self.question_text

#
# class Choice(models.Model):
#      # on_delete del question
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=100)
#     vote = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.question
