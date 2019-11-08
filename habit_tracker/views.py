from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, History
from habit_tracker.forms import HabitForm, HistoryForm
from django.utils import timezone

# Create your views here.

def home_page(request):
    creator = request.user
    all_habits = Habit.objects.all()
    return render(request, "home.html", {"all_habits": all_habits, "creator": creator })

@login_required
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


def habit_detail(request, pk): 
    habit = Habit.objects.get(pk=pk)
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.creator = request.user
            record.habit = habit
            record.save()
            return redirect (to='habit_detail', pk=pk)
    else:
        form = HistoryForm()
        records = History.objects.filter(habit=habit) 
    return render(request, "habit_detail.html", {'form': form, 'habit': habit, 'records': records})    
