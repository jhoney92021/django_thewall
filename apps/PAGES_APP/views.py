from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import random, datetime
from apps.LOGIN_APP.models import Users


def index(request): #SECONDARY INDEX IE /PAGES INDEX
    context={
        'Users': Users.objects.all(),
    }
    return render( request, 'PAGES_APP/index.html', context)

