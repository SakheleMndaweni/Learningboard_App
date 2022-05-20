from django.shortcuts import render

# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import *
from apps.home.models import * 
from apps.homeParent.models import *
from apps.homeTeacher.models import * 
from apps.homeManager.models import *


@login_required(login_url="/login/")
def indexParent(request):
    context = {'segment': 'index'}

    return render(request,"homeParent/homeParent.html",context)

@login_required(login_url="/login/")
def Parent_Events(request):
    events = Event.objects.all()
    context = {'segment': 'events','schoolEvents':events}
   
    return render(request,"homeParent/events.html",context)

@login_required(login_url="/login/")
def Parent_Communication(request):
    context = {'segment': 'communication'}

    return render(request,"homeParent/communication.html",context)

@login_required(login_url="/login/")
def Parent_Attendance(request):
    students_a = []
    parent = Parent.objects.filter(email = "user Email")
    if len(parent) == 1:
        student_ids =  Validate.objects.filter(parent_id_number = parent[0].id_number)
        for s_id in student_ids:
            student = Student.objects.get(id_number = s_id.student_id_number)
            students_a.push(student)
    
    context = {'segment': 'attendance', 'students': student_a}
    
    return render(request,"homeParent/attendance.html",context)

@login_required(login_url="/login/")
def Parent_Meetings(request):
    parent = Parent.objects.filter(email = "user Email")
    meetings = None
    if len(parent) == 1:
       meetings  = Meeting.objects.filter(invidet_id = parent[0].id_number)
    context = {'segment': 'meetings','Meetings':meetings}

    return render(request,"homeParent/meetings.html",context)

@login_required(login_url="/login/")
def Parent_Performance(request):
    students_a = []
    parent = Parent.objects.filter(email = "user Email")
    if len(parent) == 1:
        student_ids =  Validate.objects.filter(parent_id_number = parent[0].id_number)
        for s_id in student_ids:
            student = Student.objects.get(id_number = s_id.student_id_number)
            students_a.push(student)
    
    context = {'segment': 'performance','students':students}

    return render(request,"homeParent/performance.html",context)

@login_required(login_url="/login/")
def Parent_News(request):
    news = News.objects.all()
    context = {'segment': 'news','News':news}

    return render(request,"homeParent/news.html",context)

@login_required(login_url="/login/")
def Parent_Validate(request):
    parent = Parent.objects.filter(email = "user Email")
    messageStatus =''
    chec_p = []
    
    if len(parent) == 1:
       chec_p = BR_Parents_Students.objects.filter(parent_id_number = parent[0].id_number)
    search_student=[]
    if len(chec_p) == 0:
        #parent not validated and has no child
        if request.POST.get('Children_id'):
            value = request.POST.get('Children_id')
            search_student = Student.objects.filter(id_number=value)
            if len(search_student) == 1:
                BR_Parents_Students.objects.create(student_id_number=search_student[0].id_number,parent_id_number=parent[0].id_number)
                messageStatus = 'Account validated'
            else:
                messageStatus = 'Account validated'

    else:
        #parent has a chiled
        #check if current chiled is validated
        if request.POST.get('Children_id'):
            value = request.POST.get('Children_id')
            current_student =" "
        
            for c in chec_p:
                if c.student_id_number != value:
                    messageStatus = 'No student'
                    continue
            
                else:
                    messageStatus = 'Student exist'
                    break

            if messageStatus == 'No student':
                serch_student = Student.objects.filter(id_number=value)
                if len(search_student) == 0:
                    BR_Parents_Students.objects.create(student_id_number=search_student[0].id_number,parent_id_number=value)
                    messageStatus = 'Account validated'
                else:
                    messageStatus = 'Student error. Student not found'

            else:
                messageStatus = 'Student Validated'

            print('saved')

    context = {'segment': 'validate','message':messageStatus}

    return render(request,"homeParent/validate.html",context)

@login_required(login_url="/login/")
def Parent_Marks(request):
    students_a = []
    parent = Parent.objects.filter(email = "user Email")
    if len(parent) == 1:
        student_ids =  Validate.objects.filter(parent_id_number = parent[0].id_number)
        for s_id in student_ids:
            student = Student.objects.get(id_number = s_id.student_id_number)
            students_a.push(student)

    context = {'segment': 'marks','students':students_a}

    return render(request,"homeParent/marks.html",context)

@login_required(login_url="/login/")
def Parent_Homeworks(request):
    students_a = []
    parent = Parent.objects.filter(email = "user Email")
    if len(parent) == 1:
        student_ids =  Validate.objects.filter(parent_id_number = parent[0].id_number)
        for s_id in student_ids:
            student = Student.objects.get(id_number = s_id.student_id_number)
            students_a.push(student)

    context = {'segment': 'homework','students':student_a}

    return render(request,"homeParent/homework.html",context)

@login_required(login_url="/login/")
def School_Tiametable(request):
    response = "not yet"
    context = {'segment': 'Timetable coming soon'}
    return render(request,"homeParent/homework.html",context)


@login_required(login_url="/login/")
def new_meeting(request):
    teachers_data = []
    student_p = []
    parent = Parent.objects.filter(email = "user Email")
    student_ids = None
    subjects_s = []
    if len(parent) == 1:
        student_ids =  BR_Parents_Students.objects.filter(parent_id_number=parent[0].id_number)
        for s_id in student_ids:
            student_performance = Subject.objects.get(student_id_number = s_id.student_id_number)
            subjects_p.push(student_performance)

        # get subjects teachers
        for s in subjects_p:
            t = Teacher.objects.get(id_Number = s.teaacher_id_number)
            teachers_data.append(t)

    manage  = SchoolManager.objects.all()

    context = {'segment': 'meeting','teachers':teachers_data}
    return render(request,"homeParent/newmeeting.html",context,)


def create_meeting(request,id):
    teachers = Teacher.objects.get(id = id)
    parent = Parent.objects.get(email = "user Email")
    message = ''
    if request.POST:
        meeting =  Meeting()
        meeting.creator_id = parent.id_number
        meeting.res_id = teachers.id_number
        m = MeetingForm(request.POST or None,instance = objpractice )
        if m.is_valid():
           m.save()
           m = MeetingForm() 

    context = {'segment': 'meetings','form':m}
    return render(request,"homeParent/createmeeting.html",context)

def Parent_notifications(request):
    student = Student.objects.filter(email = "user Email")
    notifications = []
    if len(student) == 1:
       notifications = Notification.objects.filter(id_number = student[0].id_number)
    context = {'segment': 'notifications',
               'notifications': notifications
              }

    return render(request,"home/notifications.html",context)




@login_required(login_url="/login/")
def information_marks(request,id):
    student = Student.objects.get(id = id)
    counter =0
    marks = Mark.objects.filter(id_number = student.id_number)
    temp_marks_data = []

    for m in marks:
        display = {'subject':'','subject_code':'','t1':0,'t2':0,'t3':0,'t4':0,'total':0}
        s = Subject.objects.get(subject_code = m.subject_code)
        display['subject'] = s.name
        display['subject_code'] = s.subject_code
        display['t1'] = m.first
        display['t2'] = m.Second
        display['t3'] = m.third
        display['t4'] = m.fourth
        display['total'] = m.totalmarks
        temp = display
        temp_marks_data.append(temp) 

    context = {'segment': 'grades','Marks':marks, 'marks_data': temp_marks_data,'child':student}
    return render(request,"homeParent/informationmarks.html",context)

@login_required(login_url="/login/")
def information_performance(request,id):
    student = Student.objects.get(id = id)
    counter =0
    marks = Mark.objects.filter(id_number = student.id_number)
    temp_marks_data = []

    for m in marks:
        display = {'subject':'','subject_code':'','t1':0,'t2':0,'t3':0,'t4':0,'total':0}
        s = Subject.objects.get(subject_code = m.subject_code)
        display['subject'] = s.name
        display['subject_code'] = s.subject_code
        display['t1'] = m.first
        display['t2'] = m.Second
        display['t3'] = m.third
        display['t4'] = m.fourth
        display['total'] = m.totalmarks
        temp = display
        temp_marks_data.append(temp) 

    context = {'segment': 'grades','Marks':marks, 'marks_data': temp_marks_data,'child':student}

    return render(request,"homeParent/informationperformance.html",context)

@login_required(login_url="/login/")
def information_attendance(request,id):
    student = Student.objects.get(id = id)
    a = Attendance.objects.filter(student_id_number = student.id_number)
    context = {'segment': 'attendace','Attendance':a,'child':student}

    return render(request,"homeParent/informationattendance.html",context)

@login_required(login_url="/login/")
def information_homework(request,id):
    student = Student.objects.get(id = id)
    homeworks = Homework.objects.filter(student_id_number = student.id_number)
    
    assessment = []
    
    homeworks = Homework.objects.filter(student_id_number = student.id_number)
    for a in homeworks:
        display = {'subject':'',
                   'subject_code':'',
                   'teacher_email':'',
                   'topic':'',
                   'description':'',
                   'start':None,
                   'end_date':None,
                   'doc':None,
                   'sub_assessment':'',
                   'id':0}
        t = Teacher.objects.get(id_number = a.teacher_id_number)
        s = Subject.objects.get(subject_code = a.subject_code)
        display['subject'] = s.name
        display['subject_code'] = s.subject_code
        display['email'] = t.email
        display['topic'] = a.topic
        display['description'] = a.description
        display['start_date'] = a.start_date
        display['end_date'] = a.end_date
        display['doc'] = a.doc
        display['sub_assessment'] = a.sub_assessment
        display['id'] = a.id
        homework.append(display)
        
   
    context = {'segment': 'homework','homework':homework,'child':student}
    return render(request,"homeParent/informationhomework.html",context)   