
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path("",views.RegisterUser , name="register"),
    path("home/",views.Home, name="home"),
    path("question/<str:pk>",views.Single_Question, name="question"),
    path("profile/<str:pk>",views.User_Profile, name="profile"),
    path("edit-profile/<str:pk>",views.Edit_Profile, name="edit-profile"),
    # path("user_profile/<str:pk>",views.user_profile, name="user-profile"),



    path("add-question/", views.AddQuestion, name="add-question"),
    path("login/", views.LoginUser, name="login"),
    path("logout/", views.LogoutUser, name="logout"),
    path("delete/<str:pk>", views.DeleteProject, name='delete'),
    # path("single-question/<str:pk>", views.question, name='single-question')
    
    


    

    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
