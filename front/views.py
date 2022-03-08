from multiprocessing import context
import pdb
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
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
 
def quizlist(request, pk):
    
    quiz = Quiz.objects.filter(mock_id = pk)
    return render(request, 'quiz.html', {'quiz': quiz})   
@login_required(login_url='login')
def mocktest(request):
    mock = MockTest.objects.all()
    context ={"mock": mock}
    return render(request, 'mock_test.html',context)
@login_required(login_url='login')
def quizview(request, pk):
    quiz = Quiz.objects.get(pk =pk)
    context ={"quiz": quiz}
    return render(request, 'quiz_view.html',context)

@login_required(login_url='login')
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

         
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



@login_required(login_url='login')
def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
        
def progress_chart(request):
    user = request.user.id
    result = Result.objects.filter(user_id=user)
    # import pdb
    # pdb.set_trace()     
    context= {'result': result, 'user': user}
    return render(request, 'progress_chart.html', context)        
 
