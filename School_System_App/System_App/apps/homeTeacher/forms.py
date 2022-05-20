from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.homeParent.models import *
from apps.home.models import *
from .models import *

class MeetingForm(forms.Form):
      start = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      end = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      topic  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      creator_id= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      res_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))


      class Meta:
            model = Validate
            fields = ('res_id', 'creator_id', 'description','topic','end','start')
            
class AssessmentsForm(forms.Form):
      end_date  = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      start_date= forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "Assessment closing date and time",
                "class": "form-control"
            }
        ))
      topic  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Assessment topic",
                "class": "form-control"
            }
        ))
     
      doc= forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Assessment Docs",
                "class": "form-control"
            }
        ))
      sub_assessment = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "sub assessment",
                "class": "form-control"
            }
        ))
       
      class Meta:
            model  = Assessments
            fields = ('topic', 'description','doc','sub_assessment','start_date','end_date')



class HomeworkForm(forms.Form):
      end_date  = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "start date",
                "class": "form-control"
            }
        ))
      start_date= forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "Assessment closing date and time",
                "class": "form-control"
            }
        ))
      topic  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Assessment topic",
                "class": "form-control"
            }
        ))
     
      doc= forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Assessment Docs",
                "class": "form-control"
            }
        ))
      sub_assessment = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "sub assessment",
                "class": "form-control"
            }
        ))
       
      class Meta:
            model  = Homework
            fields = ('topic', 'description','doc','sub_assessment','start_date','end_date')




      
