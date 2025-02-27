from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, DietPlan
from .forms import WorkoutForm, DietPlanForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django. contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

User = get_user_model()  #get the correct user model dynamically
def register_user(request):
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

        messages.success(request, "Registration successful! You Can Now Log In.")
        login(request, user) #automatically log the user in after registration
        return redirect("home") #redirect to homepage
    
    return render(request, "register.html")
def login_user(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
           return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login') #redirect to login page                   

def home(request):
    return render(request, 'home.html')

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'fitness/workouts.html', {'workouts': workouts})

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
    return render(request, 'fitness/add_workout.html', {'form': form})

@login_required
def delete_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    workout.delete()
    return redirect('workout_list')

@login_required
def diet_list(request):
    diets = DietPlan.objects.filter(user=request.user)
    return render(request, 'fitness/diets.html', {'diets': diets})

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
    return render(request, 'fitness/add_diet.html', {'form': form})

@login_required
def delete_diet(request, id):
    diet = get_object_or_404(DietPlan, id=id)
    diet.delete()
    return redirect('diet_list')
    
def login(request):
    return render(request, 'login.html')
    
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'fitness/workouts.html', {'workouts': workouts})


