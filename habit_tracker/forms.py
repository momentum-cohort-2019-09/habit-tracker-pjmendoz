from django import forms
from habit_tracker.models import Habit, History
from django.forms import ModelForm


class HabitForm(forms.ModelForm):

  class Meta:
    model = Habit
    fields = ['name','quantity', 'end_date']

class HistoryForm(forms.ModelForm): 

  class Meta: 
    model = History
    fields = ['record','actual', 'date', 'met_goal']    
