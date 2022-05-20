# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts        import render, redirect
from django.contrib.auth     import authenticate, login
from .forms                  import LoginForm, SignUpForm
from apps.home.models        import *
from apps.homeManager.models import *
from apps.homeTeacher.models import *
from apps.homeParent.models  import *


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user     = authenticate(username=username, password=password)
            teacher = Teacher.objects.filter(email=user.email)
            parent  = Parent.objects.filter(email=user.email)
            student = Student.objects.filter(email=user.email)
            manager = SchoolManager.objects.filter(email=user.email)
            if user is not None:
                
                
                if len(student)==1 :
                   login(request, user)
                   return redirect("/")

                if len(parent)== 1:
                   login(request, user)
                   return redirect("Parent/")

                if len(teacher) ==1:
                   login(request, user)
                   return redirect("Teacher/")

                if len(manager) == 1:
                   login(request, user)
                   return redirect("School/")

                

            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
