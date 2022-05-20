# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file

    path('Subjects/', views.school_subjects, name='subjects'),
    path('Subject/<int:id>/', views.subjects_information, name='subjectinformation'),
    path('Assessments/', views.school_assessments, name='assessments'),
    path('Assessment/<int:id>/', views.assessment_information, name='assessmentsinformation'),
    path('Performance/', views.school_performance, name='performance'),
    path('Grades/', views.school_grades, name='grades'),
    path('Homework/',views.my_homework, name='homework'),
    path('Homework/<int:id>/',views.submission_homework, name='homeworksubmit'),
    path('classroom/',views.my_classroom, name='classroom'),
    path('Student/<int:id>/',views.student_profile, name='student'),
    path('Attendance/', views.school_attendance, name='attendance'),
    path('TimeTable/', views.school_timeTable, name='timeTable'),
    path('News/', views.school_news, name='news'),
    path('Profile/', views.my_profile, name='profile'),
    path('Notifications/', views.school_notifications, name='notifications'),
    path('Calendar/', views.school_calendar, name='calendar'),
    path('Events/', views.school_events, name='events'),
    

]
