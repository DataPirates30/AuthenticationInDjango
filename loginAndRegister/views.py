from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
# Views for login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print("You are inside post req")
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html',{"form": form})

def home_view(request):
    return render(request,'home.html')