from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm,  LoginForm
from django.contrib import messages


# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        return render(request, "home.html")
    return redirect('login')

def login_user(request):
    form = LoginForm(request.POST or None)

    msg = None

    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        return render(request, "login.html", {"form": form, "msg": msg})
    return redirect("home")
    
   

def register_user(request):
    msg = None
    success = False
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            return redirect('/login_user/')
        
        else:
            messages.error(request,"Form is not valid")
    else:
        form = SignupForm()
        
    
            
    
    return render(request,'register.html',{'form':form,'msg':msg, "success": success})

