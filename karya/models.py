from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    employee_id     = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_id


class Team(models.Model):
    team_name       = models.CharField(max_length=255)
    no_of_members   = models.IntegerField(default=0)
    members         = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

class Project(models.Model):
    pass

TASK_STATUS_CHOICE = (
        ('not started','Not Started'),
        ('in progress', 'In Progress'),
        ('on hold', 'On Hold'),
        ('completed', 'Completed'),
        ('user accepted', 'User Accepted'),
)
class Task(models.Model):
    task_title      = models.CharField(max_length=255)
    created_by      = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sample1')
    assigned_to     = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sample2')
    create_time     = models.DateTimeField()
    user_story      = models.TextField()
    status          = models.CharField(max_length=50, choices=TASK_STATUS_CHOICE, default='Select')

    def __str__(self):
        return self.task_title


# class AboutTask(models.Model):
#     task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
#     comments = models.TextField()
