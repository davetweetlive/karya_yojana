from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    employee_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    profile_img = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank = True, null = True)
    def __str__(self):
        return self.employee_id


class Team(models.Model):
    team_name   = models.CharField(max_length=255, primary_key=True)
    member      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Project(models.Model):
    name    = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by_user')
    assigned_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='assigned_to_team')
    create_time= models.DateTimeField()
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

TASK_STATUS_CHOICE = (
        ('not started','Not Started'),
        ('in progress', 'In Progress'),
        ('on hold', 'On Hold'),
        ('completed', 'Completed'),
        ('user accepted', 'User Accepted'),
)

class Task(models.Model):
    task_title      = models.CharField(max_length=255)
    created_by      = models.OneToOneField(User, on_delete=models.CASCADE, related_name='created_by')
    assigned_to     = models.OneToOneField(User, on_delete=models.CASCADE, related_name='assigned_to_user')
    create_time     = models.DateTimeField()
    user_story      = models.TextField()
    status          = models.CharField(max_length=50, choices=TASK_STATUS_CHOICE, default='select')

    def __str__(self):
        return self.task_title


# class AboutTask(models.Model):
#     task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
#     comments = models.TextField()
