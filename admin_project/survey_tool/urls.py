from django.urls import path
from . import views
urlpatterns = [
    path('', views.SurveyCreateView.as_view()),
]