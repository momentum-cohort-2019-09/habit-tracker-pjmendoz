from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History, Comment

# Create your views here.
@csrf_exempt
def home_page(request):
  user = request.user
  return render(request, "habit_tracker/home.html", {"user": user})
  
@csrf_exempt
@login_required
def home_logged_in(request): 
  habits = Habit.objects.all()
  return render(request, "habit_tracker/home_logged_in.html", {"habits": habits})