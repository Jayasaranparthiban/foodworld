from django import forms
from .models import Workout, DietPlan

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'duration']

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['meal_name', 'calories']
