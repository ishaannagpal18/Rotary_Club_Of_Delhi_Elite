from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Index.models import *
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UploadForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            email ,
            message,
            name,
            ['rcdelhielite@gmail.com']
            )
        messages.success(request, 'Your message was delivered successfully')
        contactformdata = contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()

    return render(request,'index.html')

def aboutus(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def team(request):
    return render(request, 'team.html')

def contactus(request):
    return render(request, 'contact.html')

def lobby(request):
    return render(request, 'lobby.html')

# @login_required(login_url='/')
def auditorium(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        comment = request.POST.get('comment')
        comment_obj = Comment.objects.create(fullname = fullname, comment = comment)
        comment_obj.save()
        return HttpResponseRedirect(reverse('auditorium'))


    return render(request,'auditorium.html')

def exhibition(request):
    return render(request, 'exhibition.html')

def session(request):
    return render(request, 'session.html')

def project(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UploadForm()
    img = Upload.objects.all()
    return render(request, 'project.html', {'img':img, 'form':form})

def selfie(request):
    return render(request, 'selfie.html')

def selfie2(request):
    return render(request, 'selfie2.html')

def selfie3(request):
    return render(request, 'selfie3.html')
