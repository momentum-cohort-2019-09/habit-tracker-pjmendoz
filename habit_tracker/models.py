from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    is_registered = models.BooleanField(default=False)

class Habit(models.Model):     
    creator = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="habits", null=True)
    name = models.CharField(max_length=200)
    goal = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class History(models.Model): 
    habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, related_name="records", null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    met_goal = models.BooleanField(default=False)

    def __str__(self):
        return self.habit  

class Comment(models.Model): 
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="comments", null=True)
    habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, related_name="comments", null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment