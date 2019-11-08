from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History, Comment
from habit_tracker.forms import HabitForm
from django.utils import timezone

# Create your views here.

def home_page(request):
    creator = request.user
    all_habits = Habit.objects.all()
    return render(request, "home.html", {"all_habits": all_habits, "creator": creator })


def profile_page(request):
    user = request.user
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.creator = user
            habit = form.save()
            return redirect(to='profile_page')   
    else:
        form = HabitForm()   
        user_habits = Habit.objects.filter(creator=User.objects.get(pk=request.user.pk)) 
    return render(request, "profile.html", {"user": user, "form": form, "habits": user_habits})

