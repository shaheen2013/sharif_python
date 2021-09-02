import json
from django.db.models import F
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):

    choice = (
            ('checkbox','Multi choice'),
            ('date',"Date"),
            ('email',"Email"),
            ('file',"File"),
            ('number',"Number"),
            ('radio',"Radio select"),
            ('text','Single line answer'),
            ('time',"Time"),
            ('url',"Url"),
            ('week',"Week"),
            ('select',"Dropdown"),
            ('textarea',"Text")
        )

    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    title = models.CharField(max_length=150,null=True,blank=True)
    order = models.IntegerField(null=True,blank=True)
    type = models.CharField(max_length=10,choices=choice,null=True,blank=True)
    options = models.TextField(null=True, blank=True)
    choices = models.JSONField(null=True,blank=True)



    def __str__(self):
        return f'{self.survey.title}  {self.title}'

    def save(self, *args, **kwargs):
        Question.objects.filter(order__gte=self.order).update(order=F('order')+1)
        i = 0
        for question in Question.objects.all().order_by('order'):
            i = i+1
            Question.objects.filter(id=question.id).update(order=i)
        choices = self.options.split(',')
        choice_dict = {}
        for choice in choices:
            key = choice
            choice_dict[key] = choice
        self.choices = json.loads(json.dumps(choice_dict))
        super(Question,self).save(*args, **kwargs)



class SurveyReports(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    answer = models.JSONField(null=True,blank=True)

    def __str__(self):
        return self.survey.title