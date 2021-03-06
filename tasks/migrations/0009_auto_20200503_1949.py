# Generated by Django 3.0.5 on 2020-05-03 16:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_remove_task_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default=django.utils.timezone.now, help_text='Enter a text of the task', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.TaskStatus'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
