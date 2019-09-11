from __future__ import unicode_literals
from django.db import models
from apps.LOGIN_APP.models import Users
import re, bcrypt
# Create your models here.



class Pages(models.Model):
    owner = models.ForeignKey(Users, related_name='users_page')  
    userDescription = models.TextField(max_length = 300, default='write something about yourself')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Messages(models.Model):
    creator = models.ForeignKey(Users, related_name='created_messages')
    page = models.ForeignKey(Pages, related_name='page_messages')
    content = models.TextField(max_length = 180, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    creator = models.ForeignKey(Users, related_name='created_comments') 
    message = models.ForeignKey(Messages, related_name='message_comments') 
    content = models.TextField(max_length = 180, default='') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)