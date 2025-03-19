from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Maindish, Starters
from .forms import MaindishForm, StartersForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django. contrib import messages
from django.contrib.auth import get_user_model, login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import RegisterForm
from .models import CustomUser


User = get_user_model()  #get the correct user model dynamically
def register_user(request):
    print("registre executed")
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        #check if passwords match
        if password != confirm_password:
            messages.error(request,"passwords do not match.")
            return redirect("register")
        
        #check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
            return redirect("register")
        
        #check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("register")
        
        #create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            dj_login(request, authenticated_user)

        messages.success(request, "Registration successful! You Can Now Log In.")
        dj_login(request, user) #automatically log the user in after registration
        return redirect("login") #redirect to loginpage
    
    return render(request, "register.html")


def login_user(request):
    #print(f"Trying to login: {username},{password}")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # ✅ Correct login function
            messages.success(request, f"Welcome {username}!")
            return redirect("home")  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('login') #redirect to login page                   

def home(request):
    return render(request, 'home.html')

@login_required
def maindish_list(request):
    maindish = Maindish.objects.filter(user=request.user)
    return render(request, 'maindish.html', {'maindish': maindish})

@login_required
def add_maindish(request):
    if request.method == 'POST':
        form = MaindishForm(request.POST)
        if form.is_valid():
            maindish = form.save(commit=False)
            maindish.user = request.user
            maindish.save()
            return redirect('maindish_list')
    else:
        form = MaindishForm()
    return render(request, 'add_maindish.html', {'form': form})

@login_required
def update_maindish(request, id):
    maindish = get_object_or_404(Maindish, id=id)
    if request.method == 'POST':
        form = MaindishForm(request.POST, instance=maindish)
        if form.is_valid():
            form.save()
            return redirect('maindish_list')
    else:
        form = MaindishForm(instance=maindish)
    return render(request, 'update_maindish.html', {'form': form})

@login_required
def delete_maindish(request, id):
    maindish = get_object_or_404(Maindish, id=id)
    maindish.delete()
    return redirect('maindish_list')

@login_required
def starters_list(request):
    starters = Starters.objects.filter(user=request.user)
    return render(request, 'starters.html', {'starters': starters})

@login_required
def add_starters(request):
    if request.method == 'POST':
        form = StartersForm(request.POST)
        if form.is_valid():
            starters = form.save(commit=False)
            starters.user = request.user
            starters.save()
            return redirect('starters_list')
    else:
        form = StartersForm()
    return render(request, 'add_starters.html', {'form': form})

@login_required
def update_starters(request, id):
    starters = get_object_or_404(Starters, id=id)
    if request.method == 'POST':
        form = StartersForm(request.POST, instance=starters)
        if form.is_valid():
            form.save()
            return redirect('starters_list')
    else:
        form = StartersForm(instance=starters)
    return render(request, 'update_starters.html', {'form': form})
@login_required
def delete_starters(request, id):
    starters = get_object_or_404(Starters, id=id)
    starters.delete()
    return redirect('starters_list')
    

def maindish_list(request):
    maindish = Maindish.objects.filter(user=request.user)
    return render(request, 'maindish.html', {'maindish': maindish})


