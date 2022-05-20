

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from apps.home.models import *
from apps.homeManager.models import *
from apps.homeTeacher.models import *
from apps.homeParent.models import *




class StudentForm(forms.ModelForm):
        name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Name",
                    "class": "form-control"
                }
            ))
        surname = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "surname",
                    "class": "form-control"
                }
            ))
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                    "class": "form-control"
                }
            ))
        id_number = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "id number",
                    "class": "form-control"
                }
            ))
        phone = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Pnone numbers",
                    "class": "form-control"
                }
            ))
        address = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Address",
                    "class": "form-control"
                }
            ))
        classroom = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Classroom",
                    "class": "form-control"
                }
            ))
        class Meta:
            model = Student
            fields = ('name', 'surname', 'phone', 'email','id_number')


class TeacherForm(forms.ModelForm):
        name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Name",
                    "class": "form-control"
                }
            ))
        surname = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "surname",
                    "class": "form-control"
                }
            ))
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                    "class": "form-control"
                }
            ))
        id_number = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "id number",
                    "class": "form-control"
                }
            ))
        phone = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Pnone numbers",
                    "class": "form-control"
                }
            ))
     
        class Meta:
            model = Teacher
            fields = ('name', 'surname', 'phone', 'email','id_number')
class NewsForm(forms.ModelForm):
        
        image = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "surname",
                    "class": "form-control"
                }
            ))
        topic = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "News Topic",
                    "class": "form-control"
                }
            ))
        date = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "News Date",
                    "class": "form-control"
                }
            ))
        description = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "News Description",
                    "class": "form-control"
                }
            ))
        Author = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Author",
                    "class": "form-control"
                }
            ))
        class Meta:
              model = News
              fields = ('Author', 'description', 'date', 'topic','image')

class SchoolManagerForm(forms.ModelForm):
        name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Name",
                    "class": "form-control"
                }
            ))
        surname = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "surname",
                    "class": "form-control"
                }
            ))
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                    "class": "form-control"
                }
            ))
        id_number = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "id number",
                    "class": "form-control"
                }
            ))
        phone = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Pnone numbers",
                    "class": "form-control"
                }
            ))
        address = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Address",
                    "class": "form-control"
                }
            ))
        class Meta:
            model = SchoolManager
            fields = ('name', 'surname', 'phone', 'email','id_number')



class EventsForm(forms.ModelForm):
        
        topic = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "surname",
                    "class": "form-control"
                }
            ))
        description = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                    "class": "form-control"
                }
            ))
        Startdate = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "id number",
                    "class": "form-control"
                }
            ))
        Enddate = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Pnone numbers",
                    "class": "form-control"
                }
            ))
        Author = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Address",
                    "class": "form-control"
                }
            ))
        class Meta: 
              model = Events
              fields = ('Author', 'Enddate', 'Startdate', 'description','topic')
