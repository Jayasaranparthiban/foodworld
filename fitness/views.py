from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, DietPlan
from .forms import WorkoutForm, DietPlanForm
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
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts.html', {'workouts': workouts})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'add_workouts.html', {'form': form})

@login_required
def update_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'update_workout.html', {'form': form})

@login_required
def delete_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    workout.delete()
    return redirect('workout_list')

@login_required
def diet_list(request):
    diets = DietPlan.objects.filter(user=request.user)
    return render(request, 'mydiets.html', {'diets': diets})

@login_required
def add_diet(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.user = request.user
            diet.save()
            return redirect('diet_list')
    else:
        form = DietPlanForm()
    return render(request, 'add_diet.html', {'form': form})

@login_required
def update_diet(request, id):
    diet = get_object_or_404(DietPlan, id=id)
    if request.method == 'POST':
        form = DietPlanForm(request.POST, instance=diet)
        if form.is_valid():
            form.save()
            return redirect('diet_list')
    else:
        form = DietPlanForm(instance=diet)
    return render(request, 'update_diet.html', {'form': form})
@login_required
def delete_diet(request, id):
    diet = get_object_or_404(DietPlan, id=id)
    diet.delete()
    return redirect('diet_list')
    
#def login(request):
    return render(request, 'login.html')    

def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts.html', {'workouts': workouts})


