from ast import Mod
from statistics import mode
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields

from base.models import Profile, TodoList


class CustomUserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']

class VoteForm(ModelForm):
    class Meta:
        model=TodoList
        fields=["votes_positive"]
        

class AddQuestionForm(ModelForm):
    class Meta:
        model=TodoList
        fields=['title','description','Question_pic','Answer_pic','tag_name']
        
   
class EditProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','description','email','profile_pic']
