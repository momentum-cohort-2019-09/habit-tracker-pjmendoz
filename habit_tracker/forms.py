from django import forms
from habit_tracker.models import Habit, Comment
from django.forms import ModelForm


class HabitForm(forms.ModelForm):

  class Meta:
    model = Habit
    fields = ['name','goal', 'end_date']