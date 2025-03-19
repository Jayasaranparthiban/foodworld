from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Maindish, Starters

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

class MaindishForm(forms.ModelForm):
    class Meta:
        model = Maindish
        fields = ['meal_name', 'description', 'duration']

class StartersForm(forms.ModelForm):
    class Meta:
        model = Starters
        fields = ['meal_name', 'description', 'grams', 'duration']

class UpdateMaindishForm(forms.ModelForm):
    class Meta:
        model = Maindish
        fields = ["meal_name", "description", "duration"]

class UpdateStartersForm(forms.ModelForm):
    class Meta:
        model = Starters
        fields = ["meal_name", "description", 'grams', 'duration']
        
         
