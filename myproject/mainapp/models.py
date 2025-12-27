from django.db import models

# Create your models here.
class TaskModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    due_date = models.DateField() 
    priority = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    groupby = models.CharField(max_length=100, blank=True)

class UserModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=32, null=False)