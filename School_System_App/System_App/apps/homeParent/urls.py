
from django.urls import path, re_path
from apps.homeParent import views

urlpatterns = [

    # The home page
    path('Parent/', views.indexParent, name='Parenthome'),
    path('Parent/Events/', views.Parent_Events, name='Parentevents'),
    path('Parent/Communication/', views.Parent_Communication, name='Parentcommunication'),
    path('Parent/Meetings/', views.Parent_Meetings, name='Parentmeetings'),
    path('Parent/Performance/', views.Parent_Performance, name='Parentperformance'),
    path('Parent/Performance/<int:id>/', views.information_performance, name='Parentperformanceinfor'),
    path('Parent/News/', views.Parent_News, name='Parentnews'),
    path('Parent/Validate/', views.Parent_Validate, name='Parentvalidate'),
    path('Parent/Attendance/', views.Parent_Attendance, name='Parentattendance'),
    path('Parent/Attendance/<int:id>/', views.information_attendance, name='Parentattendanceinfor'),
    path('Parent/Timetable/', views.School_Tiametable, name='schooltimetable'),
    path('Parent/meeting/new/', views.new_meeting, name='newmeeting'),
    path('Parent/meeting/new/<int:id>/', views.create_meeting, name='createmeeting'),
    path('Parent/Marks/', views.Parent_Marks, name='Parentmarks'),
    path('Parent/Marks/<int:id>/', views.information_marks, name='Parentmarksinfor'),
    path('Parent/Notification/', views.Parent_notifications, name='Parentnotifications'),
    path('Parent/Homeworks/', views.Parent_Homeworks, name='Parenthomework'),
    path('Parent/Homeworks/<int:id>/', views.Parent_Homeworks, name='Parenthomeworkinfor'),


]
