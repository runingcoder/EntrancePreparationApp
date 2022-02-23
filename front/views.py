from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from .forms import CreateUserForm
# Create your views here.
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
