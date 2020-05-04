from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, TaskStatus, Tag, User
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_statuses'] = TaskStatus.objects.all()
        context['users'] = User.objects.all()
        return context

    def get_queryset(self):
        if self.request.GET:
            parameters = self.request.GET
            filters = {}
            for key, value in parameters.items():
                if value:
                    filters[key] = value
            return Task.objects.filter(**filters)
        return Task.objects.all()


@login_required
def task(request, task_id):
    return render(request, 'task.html', context={
        'task': get_object_or_404(Task, id=task_id)
    })


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_initial(self, *args, **kwargs):
        initial = super(TaskCreate, self).get_initial(**kwargs)
        initial['creator'] = self.request.user
        return initial



class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')


# Tags views
def tags(request):
    return render(request, 'tags.html', context={
        'tags': Tag.objects.all(),
    })


@login_required
def tag(request, tag_id):
    return render(request, 'tag.html', context={
        'tag': get_object_or_404(Tag, id=tag_id)
    })


class TagCreate(CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('tags')

    def get_context_data(self, **kwargs):
        context = super(TagCreate, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagUpdate(UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('tags')
    template_name = 'tag_update.html'

    def get_context_data(self, **kwargs):
        context = super(TagUpdate, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags')


# TaskStatus views
def task_statuses(request):
    return render(request, 'task_statuses.html', context={
        'task_statuses': TaskStatus.objects.all(),
    })


@login_required
def task_status(request, task_status_id):
    return render(request, 'task_status.html', context={
        'task_status': get_object_or_404(TaskStatus, id=task_status_id)
    })


class TaskStatusCreate(CreateView):
    model = TaskStatus
    fields = '__all__'
    success_url = reverse_lazy('task_statuses')

    def get_context_data(self, **kwargs):
        context = super(TaskStatusCreate, self).get_context_data(**kwargs)
        context['task_statuses'] = TaskStatus.objects.all()
        return context


class TaskStatusUpdate(UpdateView):
    model = TaskStatus
    fields = '__all__'
    success_url = reverse_lazy('task_statuses')
    template_name = 'taskstatus_update.html'

    def get_context_data(self, **kwargs):
        context = super(TaskStatusUpdate, self).get_context_data(**kwargs)
        context['task_statuses'] = TaskStatus.objects.all()
        return context


class TaskStatusDelete(DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('task_statuses')
