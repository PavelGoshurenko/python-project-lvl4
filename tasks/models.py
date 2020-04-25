from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Enter a task name.")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, help_text="Enter a text of the task")
    STATUS_CHOICES = [
        ('1', 'status 1'),
        ('2', 'status 2'),
        ('3', 'status 3'),
        ('4', 'status 4'),
        ('5', 'status 5'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
