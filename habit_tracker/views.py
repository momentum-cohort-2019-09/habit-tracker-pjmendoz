from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History, Comment
from habit_tracker.forms import HabitForm
from django.utils import timezone

# Create your views here.

def home_page(request):
    user = request.user
    return render(request, 'home.html', {"user": user})


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
    return render(request, "profile.html", {"user": user, "form": form})


def habit_render(request, pk):
    allhabits = Habit.objects.filter(creator=request.user)
    if request.method =="POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect(to='profile_page', pk=allhabits.pk)
    else:
        form = HabitForm()
    return render(request, "profile.html", {"form": form})
