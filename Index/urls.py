from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('gallery',views.gallery,name='gallery'),
    path('team',views.team,name='team'),
    path('contactus',views.contactus,name='contactus'),
    path('lobby',views.lobby,name='lobby'),
    path('auditorium',views.auditorium,name='auditorium'),
    path('exhibition' , views.exhibition , name='exhibition'),
    path('session' , views.session , name='session'),
    path('project' , views.project , name='project'),
    path('selfie' , views.selfie , name='selfie'),
    path('selfie2' , views.selfie2 , name='selfie2'),
    path('selfie3' , views.selfie3 , name='selfie3'),
]
