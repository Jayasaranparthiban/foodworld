from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Workout, DietPlan

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match!")

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'duration']

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['meal_name', 'protien', 'grams']

class UpdateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["title", "description", "duration"]

class UpdateDietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ["meal_name", "protien", 'grams']
        
         
