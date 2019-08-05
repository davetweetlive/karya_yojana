from django.db import models
from django.contrib.auth.models import User

class TeamDetails(models.Model):
    team_name   = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.team_name


class EmployeeProfile(models.Model):
    employee_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    profile_img = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank = True, null = True)
    def __str__(self):
        return self.employee_id
