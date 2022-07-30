
from ast import Add
import profile
from pydoc import render_doc
import re
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.template import context

from base.forms import AddQuestionForm, CustomUserRegForm, VoteForm, EditProfileForm
from .models import Profile, Tags, TodoList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

# Create your views here.
def Home(request):
    
    # profile =Profile.objects.get(id=pk)
    # user_profile=Profile.objects.all()
    tasks=TodoList.objects.all()
    profile=Profile.objects.all()
    user=User.objects.all()
    
    
    
    
    context={'tasks':tasks,'profile':profile ,'user':user}
    return render(request,'base/home.html', context)

def single_user_profile(request, pk):
    profile=Profile.objects.get(id=pk)
    
    context={'profile':profile}
    return render(request, 'base/profile.html', context)
    
    
# def user_profile(request, pk):
#     profile=Profile.objects.all()
#     context={'profile':profile}
#     return render(request, 'base/profile.html', context=context)





def RegisterUser(request):
    form = CustomUserRegForm()
    context={'form':form}
    if request.method=="POST":
        form = CustomUserRegForm(request.POST)
        if form.is_valid():
            user=form.save( commit=False )
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
            
    return render(request,'base/register.html', context )



def LoginUser(request):
    
    user=User.objects.all()
    if request.method=="POST":
        username=request.POST['username'].lower()
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return redirect("/")

    
        return redirect("home")

    if request.user.is_authenticated:
        return redirect("home")


    context={}
    return render(request,'base/login.html', context)


@login_required(login_url="login")

def LogoutUser(request):
    logout(request)
    return redirect("home")


def Single_Question(request,pk):
    all_qn=TodoList.objects.all()
    
    tasks=TodoList.objects.get(id=pk)
    tags=TodoList.objects.filter(id=pk)
    user=Profile.objects.get(id=tasks.owner.id)
    
    
    if request.method=="GET":
        tasks.views+=1
        tasks.save()
   
    if request.method=="POST":
        
        tasks.votes_positive
        tasks.votes_positive+=1
        tasks.save()
        return HttpResponseRedirect(request.path_info)
    
 
   

    context={'tasks':tasks,'all_qn':all_qn,'tags':tags,'user':user}
    return render(request,'base/single_question.html', context)


@login_required(login_url="login")
def User_Profile(request,pk):
    # user_profile=User.objects.all()
    user=Profile.objects.get(id=pk)
    tasks=TodoList.objects.all()
    
    
    project=TodoList.objects.filter(owner=user.id)

    
    
    

    
    context={'project':project,'user':user,'tasks':tasks }
    return render(request, 'base/profile.html', context)



def Edit_Profile(request,pk):
    profile=Profile.objects.get(id=pk)

    form=EditProfileForm(instance=profile)
    
    context={'form':form}

    if request.method=="POST":
        form=EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect("home")

    return render(request, 'base/edit-profile.html', context)

@login_required(login_url="login")
def AddQuestion(request):
   
    form=AddQuestionForm()
    if request.method=="POST":
        question=TodoList.objects.all()
        user=User.objects.all()
        profile=Profile.objects.all()
        form=AddQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question=form.save(commit=False)
            question.owner=request.user.profile
            form.save()
            return redirect("home")


        

    context={'form':form}
    return render(request, "base/add-question.html",context)


def DeleteProject(request,pk):
    profile=request.user.profile

    task=TodoList.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('home')
    context={'task':task, 'profile':profile}

    return render(request,'base/profile.html', context)


# def question(request,pk):
#     question=TodoList.objects.get(id=pk)

#     form=QuestionForm(instance=question)
    
#     context={'form':form}

#     if request.method=="POST":
#         form=EditProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()

#             return redirect("home")

#     return render(request, 'base/edit-profile.html', context)


