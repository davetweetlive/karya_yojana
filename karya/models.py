# from django.db import models
# from django.contrib.auth.models import User
#
# class TeamDetails(models.Model):
#     team_name   = models.CharField(max_length=255)
#     description = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.team_name
#
#
# class EmployeeProfile(models.Model):
#     employee_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
#     profile_img = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank = True, null = True)
#     def __str__(self):
#         return self.employee_id
#
#
# class Project(models.Model):
#     project_name    = models.CharField(max_length=255)
#     created_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by_user')
#     assigned_team   = models.ForeignKey(TeamDetails, on_delete=models.CASCADE, related_name='assigned_to_team')
#     create_time     = models.DateTimeField()
#
# TASK_STATUS_CHOICE = (
#         ('not started','Not Started'),
#         ('in progress', 'In Progress'),
#         ('on hold', 'On Hold'),
#         ('completed', 'Completed'),
#         ('user accepted', 'User Accepted'),
# )
#
# class Task(models.Model):
#     task_title  = models.CharField(max_length=255)
#     created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_created_by')
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_assigned_to')
#     create_time = models.DateTimeField()
#     description = models.TextField()
#     status      = models.CharField(max_length=50, choices=TASK_STATUS_CHOICE, default='select')
#
#     def __str__(self):
#         return self.task_title
#
# class SubTasks(models.Model):
#     sub_task_name = models.CharField(max_length=255)
#     task_id       = models.ForeignKey(Task, on_delete=models.CASCADE)
#     dependent_on  = models.ForeignKey('self', null=True, related_name='subtasks', on_delete=models.CASCADE)
#     description   = models.TextField()
#     status        = models.CharField(max_length=50, choices=TASK_STATUS_CHOICE, default='select')
#     created_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subTasks_created_by')
#     assigned_to   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subTasks_assigned_to')
#     create_time   = models.DateTimeField()
#
# class Comment(models.Model):
#     task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
#     sub_task_id  = models.ForeignKey(SubTasks, on_delete=models.CASCADE)
#     commented_by  = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment       = models.TextField()
