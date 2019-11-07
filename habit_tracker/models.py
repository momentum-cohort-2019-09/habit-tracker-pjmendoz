from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):

    def ___str___(self): 
        return self.username

class Habit(models.Model):     
    creator = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="member", null=True)
    name = models.CharField(max_length=200)
    goal = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class History(models.Model): 
    habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=False, related_name="quirk")
    date = models.DateTimeField(default = timezone.now)
    description = models.TextField()
    met_goal = models.BooleanField(default=False)

    def __str__(self):
        return self.habit  

class Comment(models.Model): 
    creator = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="author", null=True)
    habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, related_name="routine", null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment