
from django.shortcuts import render


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def school_subjects(request):
    tempSubjects = []
    student = Student.objects.filter(email = "sakhele666@gmail.com")
    subject = None
    subjects_codes= []
    if len(student) == 1:
        subjects_codes = BR_Subjects_Students.objects.filter(id_number=student[0].id_number)


    if len(subjects_codes) > 0:
        subjects = Subject.objects.all()
        for s in subjects:
            for c in subjects_codes:
                if s.subject_code == c.subject_code:
                    tempSubjects.append(s)

    context = {'segment': 'subjects', 'Mysubjects': tempSubjects}

    return render(request,"home/subjects.html",context)

@login_required(login_url="/login/")
def subjects_information(request,id):
    subject =Subject.objects.get(id = id)
    subjects_codes = BR_Subjects_Students.objects.filter(subject_code = subject.subject_code)
    subject_students = []
    print(subjects_codes)
    students = Student.objects.all()
    for s in students:
        for c in subjects_codes:
            if s.id_number == c.id_number:
               subject_students.append(s)

    context = {'segment': 'subjects','subjectinfor':subject,'subjectstudents':students}
    subjects_codes = []
    return render(request,"home/subjectinformation.html",context)




@login_required(login_url="/login/")
def school_assessments(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
    assessment = []
    
    assessments = Assessments.objects.filter(student_id_number = student.id_number)
    for a in assessments:
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
        assessment.append(display)
        
        
    context = {'segment': 'assessments','assess': assessment}

    return render(request,"home/assessments.html",context)

@login_required(login_url="/login/")
def assessment_information(request,id):
    a = Assessments.objects.get(id = id)
    subject = Subject.objects.get(subject_code = a.subject_code)
    teachers =[]
   
    if request.POST:
       submission = Submission.objects.create(
           topic = a.topic ,
           description = a.description,
           deadline = a.end_date,
           assessment_code = a.assessment_code,
           comment ='Not Marked',
           marks =0,
           assessment_answer = request.POST.get('Answer_pdf'),
        )
    
    context = {'segment': 'assessments',
               'assessment': a,
               'subteachers':teachers,
               'as_subject':subject
               }

    return render(request,"home/assessmentinformation.html",context)


@login_required(login_url="/login/")
def school_performance(request):
    student = Student.objects.filter(email = "user Email")
    performance = []
    if len(student) == 1:
        performance = Mark.objects.filter(id_number = student[0].is_number)

    context = {'segment': 'performance','Performance': performance}
    return render(request,"home/performance.html",context)

@login_required(login_url="/login/")
def school_grades(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
    
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

    context = {'segment': 'grades','Marks':marks, 'marks_data': temp_marks_data}

    return render(request,"home/grades.html",context)
   
@login_required(login_url="/login/")
def school_attendance(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
    message ='Request attendace code from teacher'
    if request.POST.get('Attendance_code'):
       at_code = request.POST.get('Attendance_code')
       search = Attendance_code.objects.filter(code = at_code)
       if len(search) == 1:
           if search[0].status  == 'Active':
               message='Thank you for your participation. Attendance validated'
               #create attendace for logged in student
               #current_date = DateTime()
               #Attendance.objects.create(code =search[0].code ,student_id_number = student.id_number, day = current_day ,subject_code=search[0].subject_code )
           else:
               message ='Attendance code has expired'
       else:
            message ='Invalid  Attendance  code' 

    context = {'segment': 'attendance','A_message': message }
    return render(request,"home/attendance.html",context)

@login_required(login_url="/login/")
def school_timeTable(request):
    context = {'segment': 'timeTable'}
    return render(request,"home/timetable.html",context)

@login_required(login_url="/login/")
def school_events(request):
    events = Events.objects.all()
    context = {'segment': 'events','schoolEvents':events}
    
    return render(request,"home/events.html",context)

@login_required(login_url="/login/")
def school_news(request):
    mynews = News.objects.all()
    context = {'segment': 'news',
               'news':mynews
              }
    return render(request,"home/news.html",context)

@login_required(login_url="/login/")
def school_notifications(request):
    student = Student.objects.filter(email = "user Email")
    notifications = []
    if len(student) == 1:
       notifications = Notification.objects.filter(id_number = student[0].id_number)
    context = {'segment': 'notifications', 'notifications': notifications}
    return render(request,"home/notifications.html",context)

@login_required(login_url="/login/")
def school_calendar(request):
    context = {'segment': 'calendar'}

    return render(request,"home/calendar.html",context)

@login_required(login_url="/login/")
def my_profile(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
    context = {'segment': 'profile','student_i':student}

    return render(request,"home/profile.html",context)



@login_required(login_url="/login/")
def my_homework(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
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
        
   
    context = {'segment': 'homework','homework':homework}

    return render(request,"home/homework.html",context)
@login_required(login_url="/login/")
def submission_homework(request,id):
    a = Homework.objects.get(id = id)
    subject = Subject.objects.get(subject_code = a.subject_code)
    teachers =[]
   
    if request.POST.get('Answer_pdf'):
       submission = HomeworkSubmission.objects.create(
           topic = a.topic ,
           description = a.description,
           deadline = a.end_date,
           assessment_code = a.assessment_code,
           student_id_number = a.student_id_number,
           comment ='Not Marked',
           marks =0,
           assessment_answer = request.POST.get('Answer_pdf'),
        )
    
    context = {'segment': 'homework',
               'homeworks': a,
               'ho_subject':subject
               }  

    return render(request,"home/homeworksubmit.html",context)

@login_required(login_url="/login/")
def my_classroom(request):
    student = Student.objects.get(email = "sakhele666@gmail.com")
    classroom = Classrooms.objects.filter(student_id_number = student.id_number)
    context = {'segment': 'profile','Classroom':classroom}

    return render(request,"home/classroom.html",context)

@login_required(login_url="/login/")
def student_profile(request,id):
    student = Student.objects.get(id = id)
    context = {'segment': 'profile','Information':student}
    
    return render(request,"home/studentinfor.html",context)