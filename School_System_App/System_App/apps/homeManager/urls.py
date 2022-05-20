
from django.urls import path, re_path
from apps.homeManager import views

urlpatterns = [

    # The home page
    path('School/', views.indexManager, name='schoolhome'),
    #
    path('School/Students/', views.Manager_Students, name='schoolstudents'),
    path('School/Teachers/', views.Manager_Teachers, name='schoolteachers'),
    path('School/Management/', views.Manager_Management, name='management'),
    path('School/Create/Student/', views.create_students, name='createstudents'),
    path('School/Edit/Student/<int:id>/', views.update_students, name='updatestudent'),
    path('School/Create/Student/', views.create_teacher, name='createteacher'),
    path('School/Edit/Teacher/<int:id>/', views.update_teacher, name='updateteacher'),
    path('School/Create/Management/', views.create_manager, name='createmanager'),
    path('School/Edit/Management/<int:id>/', views.update_manager, name='updatemanager'),
    path('School/Create/Student/', views.create_news, name='createnews'),
    path('School/Edit/News/<int:id>/', views.update_news, name='updatenews'),
    path('School/Edit/Event/<int:id>/', views.update_event, name='updateevent'),
    path('School/New/Event/', views.create_event, name='createevent'),
    path('School/Events/', views.School_events, name='events'),
    path('School/News/', views.Manager_News, name='schoolnews'),
    path('School/Timetable/', views.indexManager, name='schooltimetables'),
    path('School/Performance/', views.Manager_Performance,name='schoolperformance'),
    path('admin/', views.Manager_Administration,name='schooladministration')


]
