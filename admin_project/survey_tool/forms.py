from django import forms
from .models import SurveyQuestions


class SurveyForm(forms.ModelForm):

    class Meta:
        model = SurveyQuestions
        fields = ['educational_content_rating','future_event','is_attending','comments']

        widgets = {
            'educational_content_rating': forms.RadioSelect(attrs={"class":"form-control"}),
            'future_event': forms.Textarea(),
            'is_attending': forms.RadioSelect(),
            'comments': forms.Textarea()
        }