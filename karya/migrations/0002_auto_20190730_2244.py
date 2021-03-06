# Generated by Django 2.2 on 2019-07-30 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('karya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_img', models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='SubTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_task_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('on hold', 'On Hold'), ('completed', 'Completed'), ('user accepted', 'User Accepted')], default='select', max_length=50)),
                ('create_time', models.DateTimeField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subTasks_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subTasks_created_by', to=settings.AUTH_USER_MODEL)),
                ('dependent_on', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='karya.SubTasks')),
            ],
        ),
        migrations.CreateModel(
            name='TeamDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='member',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user_story',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team_id',
        ),
        migrations.AlterField(
            model_name='project',
            name='assigned_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_team', to='karya.TeamDetails'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Orgenisation',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AddField(
            model_name='subtasks',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karya.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sub_task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karya.SubTasks'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karya.Task'),
        ),
    ]
