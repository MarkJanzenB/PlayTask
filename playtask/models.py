from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the built-in User model


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)  # Link project to a user

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Link task to a project
    completed = models.BooleanField(default=False)  # Track task completion status

    def __str__(self):
        return self.title
