from ast import Mod
from email.policy import default
from hashlib import blake2b
from operator import mod
from pydoc import describe
from pyexpat import model
from re import T
from statistics import mode
from tkinter.tix import Tree
from turtle import Turtle
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


    


class Tags(models.Model):
    tag=models.CharField(max_length=200,blank=True, null=True)
    
    
    def __str__(self):
        return self.tag


class Profile(models.Model):
    profile=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    projects=models.ForeignKey("TodoList", on_delete=models.CASCADE, blank=True, null=True)
    description=models.TextField(blank=True, null=True, default="This is my description")
    name=models.CharField(max_length=200, blank=True, null=True)
    profile_pic=models.ImageField(null=True, blank=True, default="default.jpg")
    followers=models.IntegerField(default=0)
    email=models.CharField(max_length=500, blank=True, null=True)
    rookie=models.BooleanField(default=False)
    average=models.BooleanField(default=False)
    professional=models.BooleanField(default=False)
    expert=models.BooleanField(default=False)
    god=models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name


class TodoList(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    Question_pic=models.ImageField(null=True, blank=True, default="default.jpg")
    Answer_pic=models.ImageField(null=True, blank=True, default="default.png")
    title=models.TextField( blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    votes_positive=models.IntegerField(default=0)
    votes_negative=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    tag_name=models.ForeignKey(Tags, on_delete=models.CASCADE, null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


