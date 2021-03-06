# Generated by Django 3.0.5 on 2020-05-03 16:13

from django.db import migrations


def add_statuses(apps, schema_editor):
    TaskStaus = apps.get_model('tasks', 'TaskStatus')
    TaskStaus(name="New").save()
    TaskStaus(name="In work").save()
    TaskStaus(name="On testing").save()
    TaskStaus(name="Completed").save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200503_1906'),
    ]

    operations = [
        migrations.RunPython(add_statuses),
    ]
