from django.shortcuts import render, redirect

# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import *
from apps.homeTeacher.models import *
from .models import *
from apps.homeParent.models import *
from apps.homeManager.forms import *

@login_required(login_url="/login/")
def indexManager(request):
    context = {'segment': 'index'}

    return render(request,"homeManager/schoolHome.html",context)

@login_required(login_url="/login/")
def Manager_Students(request):
    students = Student.objects.all()

    context = {'segment': 'students','allStudents':students}

    return render(request,"homeManager/students.html",context)

@login_required(login_url="/login/")
def Manager_Teachers(request):
    teachers = Teacher.objects.all()
    context = {'segment': 'teacher','teachers':teachers}
    return render(request,"homeManager/teachers.html",context)

@login_required(login_url="/login/")
def Manager_Management(request):
    management = SchoolManager.objects.all()
    context = {'segment': 'management','management':management}
    return render(request,"homeManager/management.html",context)

@login_required(login_url="/login/")
def Manager_News(request):
    news = News.objects.all()
    context = {'segment': 'news','News':news}
    return render(request,"homeManager/news.html",context)

@login_required(login_url="/login/")
def Manager_Timetable(request):
    context = {'segment': 'timetable'}
    return render(request,"homeManager/timetable.html",context)

@login_required(login_url="/login/")
def Manager_Performance(request):
    marks = Mark.objects.all()
    context = {'segment': 'performance','marks':marks}

    return render(request,"homeManager/performance.html",context)

@login_required(login_url="/login/")
def Manager_Administration(request):

    context = {'segment': 'index'}
    
    return redirect("admin/")


@login_required(login_url="/login/")
def create_students(request):
    addstudentform =  StudentForm(request.POST or None)
    if addstudentform.is_valid():
        addstudentform.save()
        addstudentform =StudentForm()
    context = {'segment': 'students','form':addstudentform}

    return render(request,"homeManager/createstudent.html",context)

@login_required(login_url="/login/")
def update_students(request,id):
    s = Student.objects.get(id = id)
    addstudentform =  StudentForm(request.POST or None)
    if addstudentform.is_valid():
        addstudentform.save()
        addstudentform =StudentForm()
    context = {'segment': 'students','form':addstudentform}

    return render(request,"homeManager/updatestudent.html",context)

@login_required(login_url="/login/")
def create_teacher(request):
    teacherform = TeacherForm(request.POST or None)
    if teacherform.is_valid():
        teacherform.save()
        teacherform = TeacherForm()
    context = {'segment': 'teachers','form':teacherform}

    return render(request,"homeManager/createteacher.html",context)

@login_required(login_url="/login/")
def update_teacher(request,id):
    t = Teacher.objects.get(id =id)
    teacherform = TeacherForm(request.POST or None)
    if teacherform.is_valid():
        teacherform.save()
        teacherform = TeacherForm()
    context = {'segment': 'performance','form':teacherform}

    return render(request,"homeManager/updateteacher.html",context)

@login_required(login_url="/login/")
def create_manager(request):
    managementform = SchoolManagerForm(request.POST or None)
    if managementform.is_valid():
        managementform.save()
        managementform = SchoolManagerForm()

        print('saved')
    context = {'segment': 'performance','form':managementform}

    return render(request,"homeManager/createmanager.html",context)
    

@login_required(login_url="/login/")
def update_manager(request,id):
    m = SchoolManager.objects.get(id = id)
    managementform = SchoolManagerForm(request.POST or None)
    if managementform.is_valid():
        managementform.save()
        managementform = SchoolManagerForm()

        print('saved')
    context = {'segment': 'performance','form':managementform}

    return render(request,"homeManager/updatemanager.html",context)


@login_required(login_url="/login/")
def create_news(request):
    nf = NewsForm(request.POST or None)
    if nf.is_valid():
       nf.save()
       nf = NewsForm()
    context = {'segment': 'news','form':nf}
    return render(request,"homeManager/createnews.html",context)

@login_required(login_url="/login/")
def update_news(request,id):
    n = News.objects.get(id = id)
    nf = NewsForm(request.POST or None)
    if nf.is_valid():
       nf.save()
       nf = NewsForm()
    context = {'segment': 'news','form':nf}

    return render(request,"homeManager/updatenews.html",context)

@login_required(login_url="/login/")
def School_events(request):
    e = Events.objects.all()
    context = {'segment': 'performance','events':e}

    return render(request,"homeManager/events.html",context)

@login_required(login_url="/login/")
def update_event(request,id):
    e = Events.objects.get(id = id)
    eventsform = EventsFormm(request.POST or None)
    if eventsform.is_valid():
        eventsform.save()
        eventsform = EventsForm()

        print('saved')
    context = {'segment': 'performance','form':eventform}

    return render(request,"homeManager/updateevent.html",context)

@login_required(login_url="/login/")
def create_event(request):
    eventform = EventsForm(request.POST or None)
    if eventform.is_valid():
        eventform.save()
        eventform = EventsForm()

        print('saved')
    context = {'segment': 'performance','form':eventform}

    return render(request,"homeManager/createevent.html",context)










