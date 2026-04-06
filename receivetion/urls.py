from django import views
from django.contrib import admin
from django.urls import path
from .views import home,register,events,gallery,ideas,contact, success,register_user
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path("register_user/", register_user, name="register_user"),
    path('success/', success, name='success'),
    path('register/', register, name='register'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('ideas/', ideas, name='ideas'),
    path('contact/', contact, name='contact'),
    path('send-mails/', views.permession_mail, name='send_mails'),
    path('take-idea/', views.take_idea, name='take_idea'),
    path("invitation/",views.invitation,name="invitation_mail"),
    path("club_invitation/",views.club_invitation,name="club_invitation"),
    path("club_permission/",views.permession_mail,name="club_permission"),
    path("senior_invitation/",views.send_cr_mail,name="senior_invitation"),
    path("batch_invitation/",views.send_bachmate_mail,name="batch_invitation"),
]
