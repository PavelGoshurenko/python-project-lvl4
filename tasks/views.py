from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    return render(request, 'index.html', context={
        'tasks': Task.objects.all(),
    })
