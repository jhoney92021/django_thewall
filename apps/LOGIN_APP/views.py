from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
import random, datetime, bcrypt


def index(request): #PRIMARY INDEX IE LOGIN INDEX
    context ={

    }
    return render(request, 'LOGIN_APP/index.html', context)

def process(request): #directory route
    return redirect('success')

def processRegistration(request): #registration route
    errors = Users.objects.validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
            return redirect('/')
    else:
        newUserPass = request.POST['password']
        newUserPassEncrypt = bcrypt.hashpw(newUserPass.encode(), bcrypt.gensalt())

        newUser = Users.objects.create(fname= request.POST['fname'], lname= request.POST['lname'], email= request.POST['email'], password= newUserPassEncrypt)
        request.session['user_live'] = newUser.id
        return redirect('/success')

def processLogin(request): #login route    
    errors = Users.objects.loginVal(request.POST)
    if len(errors) > 1:
        for key, val in errors.items():
            messages.error(request, val)
            return redirect('/')
    else:
        passGiven = request.POST['password']
        userQuery = Users.objects.get(email= request.POST['email'])
        if bcrypt.checkpw(passGiven.encode(), userQuery.password.encode()):
            request.session['user_live'] = userQuery.id
            return redirect('/success' )

        else:
            messages.error(request, 'logFail')
            return redirect('/')    

def success(request): #success route
    liveUser = request.session['user_live']
    context ={
        'user': Users.objects.get(id = liveUser),

    }
    return render(request, 'LOGIN_APP/success.html', context)

def logout(request): #logout
    request.session.clear()
    return redirect('/')