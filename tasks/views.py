from django.shortcuts import render, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'index.html', context={
        'tasks': Task.objects.all(), 'num_visits':num_visits,
    })

@login_required
def task(request, task_id):
    return render(request, 'task.html', context={
        'task': get_object_or_404(Task, id=task_id)
    })



class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name','content','status']
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
