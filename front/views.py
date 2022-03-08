from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http.response import JsonResponse
from .forms import CreateUserForm
import requests



from django.db import transaction

@transaction.atomic
def getapi(request):
    response= requests.get('https://opentdb.com/api.php?amount=50&category=22&difficulty=medium&type=multiple')
    for ques in response.json()['results']:
        question = Question.objects.create(text= ques['question'],quiz_id = '12')
        Answer.objects.create(text=ques['correct_answer'], correct=1, question_id=question.id)
        for ans in ques['incorrect_answers']:
            Answer.objects.create(text=ans,correct=0,question_id=question.id)
    return JsonResponse({"message": "sucessfully imported"})

def index1(request):
     return render(request, 'index1.html')
def index(request):
     return render(request, 'index.html')
     
def reading_material(request):
     return render(request, 'reading_materials.html')  

def mock_test(request):
     return render(request, 'mock_test.html')          
def progress(request):
     return render(request, 'progress.html')          

def registerPage(request):
    form =CreateUserForm()
    if request.method == "POST":
            form =CreateUserForm(request.POST)
            if form.is_valid():
                user =form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, "Account successfully created for " + username)
                
                return redirect('login')

        
    context ={'form': form}
    return render(request, 'register.html', context)     

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # yo get gareko, is associated with the name in the form that is posted/submitted(in the login)
        user =authenticate(request, username =username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or password is not correct")    


    context ={}
    return render(request, 'login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('login')
def terms(request):
     return render(request, 'terms.html')
 
def privacy(request):
     return render(request, 'privacy.html') 
  
def services(request):
     return render(request, 'services.html') 
 
def about(request):
     return render(request, 'about.html') 
 
def send_email_contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = ''' New message: {} 
        From: {}
        
        '''.format(data['subject'], data['email'])
        messages.success(request, "Message succesfully sent. We will reach out to you as soon as possible! ")
        send_mail(data['message'], message, '',  ['075bei005.achyut@pcampus.edu.np']) 
        
    return render(request, 'contact.html')     