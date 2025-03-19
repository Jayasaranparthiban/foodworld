from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),  # ✅ Use login_user
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='home'),
    path('maindish', views.maindish_list, name='maindish_list'),
    path('add-maindish/', views.add_maindish, name='add_maindish'),
    path('update-maindish/<int:id>/', views.update_maindish, name='update_maindish'),
    path('delete-maindish/<int:id>/', views.delete_maindish, name='delete_maindish'),
    
    path('starters/', views.starters_list, name='starters_list'),
    path('add-starters/', views.add_starters, name='add_starters'),
    path('update-starters/<int:id>/', views.update_starters, name='update_starters'),
    path('delete-starters/<int:id>/', views.delete_starters, name='delete_starters'),
]
