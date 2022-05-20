from django.shortcuts import render

# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import *
from apps.homeParent.models import *
from apps.homeTeacher.models import *
from apps.homeManager.models import *
from apps.homeTeacher.forms import *
import random
import datetime



@login_required(login_url="/login/")
def indexTeacher(request):
    context = {'segment': 'indexhome'}

    return render(request,"homeTeacher/homeTeacher.html",context)


@login_required(login_url="/login/")
def Teacher_Students(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    parents_objs = []
    t_s = []
    students = []
    s =  Subject.objects.filter(teacher_id_number = teacher[0].id_number)
    for sub in s:
        st = BR_Subjects_Students.objects.filter(subject_code = sub.subject_code)
        t_s.extend(st)
    # filter students
    for f_s in t_s:
        if f_s in students:
            continue
        else:
            students.append(f_s)
    
    # Get parent id's
    for temp in students:
        st = Student.objects.get(id_number = temp.student_id_number)
        parents_objs.append(st)

    context = {'segment': 'students','MyStudents':parents_objs}

    return render(request,"homeTeacher/students.html",context)

@login_required(login_url="/login/")
def Teacher_Subjects(request):
    teacher  = Teacher.objects.filter(email ="Zodwe@gmail.com")
    subjects = None
    for t in teacher:
       subjects = Subject.objects.filter(teacher_id_number =t.id_number)
    context = {'segment': 'subjects','MySubject':subjects}

    return render(request,"homeTeacher/subjects.html",context)

@login_required(login_url="/login/")
def Teacher_Marks(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    students_objs = []
    t_s = []
    student_infor = []
    marks = []
    students = []
    student_marks = {'student':None,'teacher':None,'marks':None}
    s =  Subject.objects.filter(teacher_id_number = teacher[0].id_number)
    for sub in s:
        st = BR_Subjects_Students.objects.filter(subject_code = sub.subject_code)
        t_s.extend(st)
    # filter students
    
    # Get parent id's
    for temp in t_s:
        st = Student.objects.get(id_number = temp.id_number)
        subject_marks = Marks.objects.get(id_number = temp.id_number)
        student_ids = BR_Subjects_Students.objects.get(id_number = st.id_number)
        
        subject_infor = Subject.objects.get()
        students_objs.append(st)



    context = {'segment': 'students','MyStudents':students_objs}

    return render(request,"homeTeacher/marks.html",context)

@login_required(login_url="/login/")
def Teacher_Assessment(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    my_assessments = None
    for a in teacher:
        my_assessments = Assessments.objects.filter(teacher_id_number = a.id_number)

    context = {'segment': 'assessment','my_assessments':my_assessments}
    return render(request,"homeTeacher/assessment.html",context)

@login_required(login_url="/login/")
def Teacher_select_subject(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    subjects = Subject.objects.filter(teacher_id_number = teacher[0].id_number)

    context = {'segment': 'assessment','mySubjects':subjects}
    return render(request,"homeTeacher/selectSubjectA.html",context)

@login_required(login_url="/login/")
def Teacher_update_Assessment(request,id):
    a =  AssessmentForm(request.POST or None)
    if a.is_valid():
        a.save()
        a = AssessmentForm()
    context = {'segment': 'assessment','form':a}
    return render(request,"homeTeacher/editHomework.html",context)


@login_required(login_url="/login/")
def Teacher_create_Assessment(request,id):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    subject =  Subject.objects.get(id = id)
    if request.POST:
       Assessments.objects.create(
       topic             = request.POST.get('topic'),
       description       = request.POST.get('description'),
       end_date          = request.POST.get('End_date'),
       start_date        = request.POST.get('start_date'),
       teacher_id_number = teacher.id_number,
       doc               = request.POST.get('doc'),
       sub_assessment    = request.POST.get('Notes'),
       assessment_code   = subject.name + subject.subject_code,
       subject_code      = subject.subject_code)

    context = {'segment': 'assessment'}

    return render(request,"homeTeacher/newAssessment.html",context)


@login_required(login_url="/login/")
def Teacher_homeworks(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    my_assessments = None
    for a in teacher:
        my_assessments = Homeworks.objects.filter(teacher_id_number = a.id_number)

    context = {'segment': 'assessment','my_assessments':my_assessments}
    return render(request,"homeTeacher/homework.html",context)

@login_required(login_url="/login/")
def Teacher_select_subject_H(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    subjects = Subject.objects.filter(teacher_id_number = teacher[0].id_number)

    context = {'segment': 'assessment','mySubjects':subjects}
    return render(request,"homeTeacher/selectSubjectH.html",context)


@login_required(login_url="/login/")
def Teacher_update_Homework(request,id):
    h =  HomeworkForm(request.POST or None)
    if h.is_valid():
        h.save()
        h = HomeworkForm()
    context = {'segment': 'students','form':h}
    return render(request,"homeTeacher/editHomework.html",context)


@login_required(login_url="/login/")
def Teacher_create_Homework(request,id):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    subject =  Subject.objects.get(id = id)
    if request.POST:
       Homework.objects.create(
       topic             = request.POST.get('topic'),
       description       = request.POST.get('description'),
       end_date          = request.POST.get('End_date'),
       start_date        = request.POST.get('start_date'),
       teacher_id_number = teacher.id_number,
       doc               = request.POST.get('doc'),
       sub_assessment    = request.POST.get('Notes'),
       assessment_code   = subject.name + subject.subject_code,
       subject_code      = subject.subject_code)

    
    return render(request,"homeTeacher/newHomework.html",context)

@login_required(login_url="/login/")
def Teacher_Events(request):
    events = Event.objects.all()
    context = {'segment': 'events','myevents':events}

    return render(request,"homeTeacher/teacherevents.html",context)

@login_required(login_url="/login/")
def Teacher_Notification(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    noti = None
    if len(teacher) == 1:
       noti = Notification.objects.filter(id_number = teacher[0].id_number)
    context = {'segment': 'notification','mynotification':noti}
    
    return render(request,"homeTeacher/notification.html",context)

@login_required(login_url="/login/")
def Teacher_Cards(request):
    context = {'segment': 'reportcards'}

    return render(request,"homeTeacher/reportcards.html",context)

@login_required(login_url="/login/")
def Teacher_Lectures(request):
    context = {'segment': 'index'}

    return render(request,"homeTeacher/lectures.html",context)

@login_required(login_url="/login/")
def Teacher_Communication(request):
    context = {'segment': 'communication'}

    return render(request,"homeTeacher/communication.html",context)

@login_required(login_url="/login/")
def Teacher_Meetings(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    meetings = None
    if len(teacher) == 1:
       meetings = Meeting.objects.filter(creator_id = teacher[0].id_number)
   
    context = {'segment': 'meetings','Mymeetings':meetings}

    return render(request,"homeTeacher/meetings.html",context)

@login_required(login_url="/login/")
def Teacher_Meetings_create(request,id):
    parent = Parent.objects.get(id = id)
    myform = None
    if parent != None:
       meeting = Meeting()
       meeting.res_id = parent.id_number
       myform = MeetingForm(request.POST or None,instance=meeting)
       if myform.is_valid():
          myform.save()
          myform = MeetingForm()



@login_required(login_url="/login/")
def Teacher_Performance(request):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    marks = []
    mystudents = None
    if len(teacher) == 1:
       mystudents =  Classrooms.objects.filter(teacher_id_number=teacher[0].id_number)

    for s in mystudents:
        tm = Marks.objects.get(student_id_number=s.student_id_number)
        marks.push(tm)
    sub = None
    if len(teacher) == 1:
        sub =  Subject.objects.filter(teacher_id_number = teacher[0].id_number)
    students = []
    for sb in sub:
        sub_students = BR_Subjects_Students.objects.filter(subject_code = sb.subject_code)
        students.append(sub_students)

    #get subjects marks Marks
    marks_S = []

    for m in students:
        tm = Marks.objects.filter(m.student_id_number)
        marks_S.append(tm)

    context = {'segment': 'performance','classmarks':marks,'subjectsMarks':marks_S}

    return render(request,"homeTeacher/performance.html",context)

@login_required(login_url="/login/")
def Teacher_News(request):
    news = News.objects.all()
    context = {'segment': 'news','mynews':news}
    return render(request,"homeTeacher/teachetnews.html",context)

@login_required(login_url="/login/")
def Teacher_Profile(request):
    teacher  = Teacher.objects.filter(email ="Zodewa@gmail.com")
    context = {'segment': 'profile','profile':teacher}

    return render(request,"homeTeacher/profile.html",context)


def Attandance(request):
    teacher  = Teacher.objects.get(email ="Zodwa@gmail.com")
    subjects  = Subject.objects.filter(teacher_id_number = teacher.id_number)
    
    context = {'segment': 'profile','subject':subjects}
    return render(request,"homeTeacher/profile.html",context)


def Teacher_Gen_Attandance(request,id):
    subject  = Subject.objects.get(id = id )
    genCode =  'ABCDEFGHIJKLMNOPQRSTUVXYZ123456789'
    Code = ''
    

    x = datetime.datetime.now()

    if request.POST:
        for i in range(5):
            Code = Code + random.choice(genCode)

        Attendance_code.objects.create(
        day               = x,
        code              = Code,
        teacher_id_number = subject.teacher_id_number,
        subject_code      = subject.subject_code,
        status            = "Valid"
        )
        
    context = {'segment': 'profile','A_code':Code}
    return render(request,"homeTeacher/profile.html",context)

@login_required(login_url="/login/")
def new_meeting(request):
    student_parent = {'teacher':None,'student':None}
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    parents  = Parent.objects.all()
    parents_temp = []
    t_s = []
    students = []
    s =  Subject.objects.filter(teacher_id_number = teacher[0].id_number)
    for sub in s:
        st = BR_Subjects_Students.objects.filter(subject_code = sub.subject_code)
        t_s.extend(st)
    # filter students
    for f_s in t_s:
        if f_s in students:
            continue
        else:
            students.append(f_s)
    
    # Get parent id's
    for temp in students:
        pa =  BR_Parents_Students.objects.filter(student_id_number = temp.id_number)
        if len(pa) == 1:
           p  = Parent.objects.get(id_number = pa[0].parent_id_number) 
           st = Student.objects.get(id_number = pa[0].student_id_number)
           student_parent['parent'] = p
           student_parent['student'] = st
           parents_temp.append(student_parent)
        else:
           for pt in pa:
               mp  = Parent.objects.get(id_number = pt.parent_id_number) 
               st = Student.objects.get(id_number = pt.student_id_number)
               student_parent['parent'] = p
               student_parent['student'] = st
               parents_temp.append(student_parent)

    manage  = SchoolManager.objects.all()

    context = {'segment': 'meeting','parents':parents_temp,'management':manage}
    return render(request,"homeParent/newmeeting.html",context,)


def create_meeting(request,id):
    teacher  = Teacher.objects.filter(email ="Zodwa@gmail.com")
    parent = Parent.objects.get(id = id)
    m = ''
    if request.POST:
        if request.POST.get('start') and request.POST.get('end') and request.POST.get('topic') and request.POST.get('description'):
            creator_id = teacher[0].id_number
            res_id = parent.id_number
            start = request.POST.get('start')
            end = request.POST.get('end')
            topic = request.POST.get('topic')
            description = request.POST.get('description')
            Meeting.objects.create(
                creator_id = creator_id,
                res_id = res_id,
                start = start,
                end = end,
                topic = topic,
                description = description
            )
            m ='Meeting created'

        else:
            m ='Invalid complete form!'

    context = {'segment': 'meetings','message':m}
    return render(request,"homeParent/createmeeting.html",context)
