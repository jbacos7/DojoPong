# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        today = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
        
        if len(postData['firstName']) < 2 or len(postData['firstName']) > 255:
            errors["firstName"] = "first name field should not be empty or greater than 255 characters"

        if len(postData['lastName']) < 2 or len(postData['lastName']) > 255:
            errors["lastName"] = "last name field should not be empty"

        if hasNum(postData['firstName']):
            errors['lastname'] = "first name can not have a number"
            
        if hasNum(postData['lastName']):
            errors['lastName'] = "last name can not have a number"

        if len(postData['username']) < 4 

        if postData['password'] != postData['confirmPass']:
            errors['password'] = "passwords do not match"

        if len(postData['password']) < 8:
            errors['password'] = "password must be greater than 8 characters"

        if matchEmail(postData['email']) == False:
            errors['email'] =  "email is not correct format"

        if len(postData['dob']) < 1:
            errors['dob'] = "date of birth field must not be empty"
        
        if (postData['dob'] > today):
            errors["dob"] = "date of birth must not be greater than todays date"
        
        return errors


class ScoreManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if ( postData['user_points'] < 7 and postData['opponent_points'] < 7 ):
            errors["quote"] = "One player must win by at least 7 points"
        
        return errors   


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Record(models.Model):
    opponent = models.OneToOneField(User)
    wins = models.IntegerField()
    losses = models.IntegerField()
    score = models.ForeignKey( )
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RecordManager()


class Score(models.Model):
    user_points = models.IntegerField()
    opponent_points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ScoreManager()
    

def matchEmail(e):
    return bool(re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', e))

def hasNum(someStr):
    return any(char.isdigit() for char in someStr)