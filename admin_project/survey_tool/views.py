from django.shortcuts import render,HttpResponse,redirect
from django.views import generic
from .models import SurveyQuestions
from .forms import SurveyForm

# class SurveyToolsView(generic.View):
#
#     def get(self,request):
#         form = SurveyForm()
#         return render(request, 'index.html', {"form": form})
#
#     def post(self,request):
#         survey = SurveyForm(request.POST)
#         if survey.is_valid():
#             survey.save()
#             return redirect('/')
#         else:
#             return redirect('/survey')


class SurveyCreateView(generic.CreateView):
    model = SurveyQuestions
    form_class = SurveyForm
    template_name = 'index.html'
    success_url = '/'