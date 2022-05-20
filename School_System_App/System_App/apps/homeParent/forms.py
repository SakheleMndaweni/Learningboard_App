from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ValidateForm(forms.Form):
      student_id_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

      class Meta:
            model = Validate
            fields = ('status', 'parent_id', 'student_id')


class MeetingForm(forms.Form):
       topic = forms.CharField(
            widget=forms.TextInput(
            attrs={
                "placeholder": "Meeting Topic",
                "class": "form-control"
              }
             ))

       description = forms.CharField(
            widget=forms.TextInput(
            attrs={
                "placeholder": "Meeting Topic",
                "class": "form-control"
              }
             ))

       end =  forms.DateTimeField(
            widget=forms.DateTimeInput(
            attrs={
                "placeholder": "Enter Start date",
                "class": "form-control"
              }
             ))

       start = forms.DateTimeField(
            widget=forms.DateTimeInput(
            attrs={
                "placeholder": "Enter End date",
                "class": "form-control"
              }
             ))

    

       class Meta:
            model = Meeting
            fields = ('topic', 'description', 'start','end')
