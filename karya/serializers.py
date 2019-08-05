from rest_framework import serializers
from django.contrib.auth.models import User

from .models import(
    EmployeeProfile,
    Project,
    Task,
    SubTasks,
    Comment
)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('project_name', 'created_by', 'assigned_team', 'create_time')
        # fields = __all__
