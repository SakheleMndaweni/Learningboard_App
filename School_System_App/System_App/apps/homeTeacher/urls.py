
from django.urls import path, re_path
from apps.homeTeacher import views

urlpatterns = [

    # The home page
    path('Teacher/', views.indexTeacher, name='Teacherhome'),
    path('Teacher/Students/', views.Teacher_Students, name='teacherstudents'),
    path('Teacher/Subjects/', views.Teacher_Subjects, name='teachersubjects'),
    path('Teacher/Marks/', views.Teacher_Marks, name='teachermarks'),
    path('Teacher/Assessment/', views.Teacher_Assessment, name='teacherassessment'),
    path('Teacher/Assessment/Subjects/', views.Teacher_select_subject, name='teachersubjectassessment'),
    path('Teacher/Assessment/New/<int:id>/', views.Teacher_create_Assessment, name='teachernewassessment'),
    path('Teacher/Assessment/Edit/<int:id>/', views.Teacher_update_Assessment, name='teachereditassessment'),
    path('Teacher/homework/', views.Teacher_homeworks, name='teacherhomework'),
    path('Teacher/homework/Subjects/', views.Teacher_select_subject_H, name='teachersubjecthomework'),
    path('Teacher/homework/New/<int:id>/', views.Teacher_create_Homework, name='teachernewhomework'),
    path('Teacher/homework/Edit/<int:id>/', views.Teacher_update_Homework, name='teacheredithomework'),
    path('Teacher/Events/', views.Teacher_Events, name='teacherevents'),
    path('Teacher/Notification/', views.Teacher_Notification, name='teachernotification'),
    path('Teacher/Cards/', views.Teacher_Cards, name='teachercards'),
    path('Teacher/Lectures/', views.Teacher_Lectures, name='teacherlectures'),
    path('Teacher/Communication/', views.Teacher_Communication, name='teachercommunication'),
    path('Teacher/Meetings/', views.Teacher_Meetings, name='teachermeetings'),
    path('Teacher/Performance/', views.Teacher_Performance, name='teacherperformance'),
    path('Teacher/News/', views.Teacher_News, name='teachernews'),
    path('Teacher/Profile/', views.Teacher_Profile, name='teacherprofile'), 
    
]
