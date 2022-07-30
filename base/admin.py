from atexit import register
from django.contrib import admin
from .models import Profile, Tags, TodoList


# Register your models here.
admin.site.register(Profile)
admin.site.register(TodoList)
admin.site.register(Tags)

