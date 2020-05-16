import django_filters
from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'creator', 'assigned_to']
