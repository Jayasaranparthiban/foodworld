from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout, DietPlan
from .forms import WorkoutForm, DietPlanForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') #redirect to home after signup
    else:
        form = RegisterForm()
    return render(request, 'fitness/register.html', {'form':form})

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
        form = AuthenticationForm()
    return render(request, 'fitness/login.html', {'form': form})

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
    


