from django import forms
from .models import Workout, DietPlan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username","email","password"]
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'duration']

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['meal_name', 'calories']
