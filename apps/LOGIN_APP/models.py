from __future__ import unicode_literals
from django.db import models
import re, bcrypt, datetime

class Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        emailFormat = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2: #check for name length
            errors['fname'] = 'Wrong Again Bob, fname to short'
        if len(postData['lname']) < 2: #check for name length
            errors['lname'] = 'Wrong Again Bob, lname taken'
        if not emailFormat.match(postData['email']): #check for email format
            errors['email'] = 'cmon, use an actualy email......'
        if len(postData['email']) < 2: #check for email length
            errors['email'] = 'email to short'
        if len(postData['password']) < 1 :
            errors['passlen'] = 'Passwords field cannot be empty'

        if postData['fname'] in Users.objects.filter(fname=postData['fname']): #check for name uniqueness
            errors['fname'] = 'Wrong Again Bob, fname taken'
        if postData['lname'] in Users.objects.filter(lname=postData['lname']): #check for name uniqueness
            errors['lname'] = 'Wrong Again Bob, lname taken'
        if postData['email'] in Users.objects.filter(email=postData['email']): #check for email uniqueness
            errors['email'] = 'Wrong Again Bob, email taken'
        if postData['password'] != postData['confirmation']: #check for pw match
            errors['password'] = 'Wrong Again Bob, passwords do not match'

        return errors

class Users(models.Model):
    fname = models.CharField(max_length=20, default='A person with no name apparently')
    lname = models.CharField(max_length=20, default='A person with no name apparently')
    username = models.CharField(max_length=20, default='not a required field')
    birthday = models.DateField(default= datetime.date.today)
    email = models.CharField(max_length=80, default='Seriously, no email? it is 2019 get with it man')
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

