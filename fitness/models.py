from django.db import models

from django.contrib.auth.models import User

class Workout(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)#on_delete=models.CASCADE ensures that if a user is deleted, their associated workouts are removed,
    title= models.CharField(max_length=255)
    description= models.TextField()
    duration= models.IntegerField(help_text="Duration in minutes")
    date= models.DateField(auto_now_add=True)#This helps in tracking daily progress without requiring manual input

    objects= models.Manager()
    
    def __str__(self):
        return str(self.title)#making it easier to identify records in the Django Admin panel
    
class DietPlan(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE ensures that if a user is deleted, their diet plans are removed
    meal_name= models.CharField(max_length=255)
    calories= models.IntegerField()
    date= models.DateField(auto_now_add=True)
    
    objects= models.Manager()#This helps in tracking daily progress without requiring manual input
    
    def __str__(self):
        return str(self.meal_name)#making it easier to identify records in the Django Admin panel
        
    
    