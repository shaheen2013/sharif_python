from django.db import models


class SurveyQuestions(models.Model):
    rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    options=(
        ("Yes",'Yes'),
        ("No",'No')
    )

    educational_content_rating = models.IntegerField(choices=rating,null=True,blank=True)
    future_event = models.TextField(null=True,blank=True)
    is_attending = models.CharField(choices=options,max_length=3,blank=True,null=True)
    comments = models.TextField(null=True,blank=True)

