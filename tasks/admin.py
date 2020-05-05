from django.contrib import admin

# Register your models here.
from .models import Tag, Task, TaskStatus

admin.site.register(Tag)
admin.site.register(TaskStatus)
admin.site.register(Task)
