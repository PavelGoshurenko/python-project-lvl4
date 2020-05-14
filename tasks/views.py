from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.models import Tag, Task, TaskStatus, User


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


""" def task(request, task_id):
    return render(request, 'task.html', context={
        'task': get_object_or_404(Task, id=task_id)
    }) """


class TaskView(generic.DetailView):
    model = Task
    template_name = "task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_initial(self, *args, **kwargs):
        initial = super(TaskCreate, self).get_initial(**kwargs)
        initial['creator'] = self.request.user
        initial['status'] = get_object_or_404(TaskStatus, name="New")
        return initial


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')


# Tags views
def tags(request):
    return render(request, 'tags.html', context={
        'tags': Tag.objects.all(),
    })


class TagsView(generic.ListView):
    template_name = 'tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class TagView(generic.DetailView):
    model = Tag
    template_name = "tag.html"


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('tags')

    def get_context_data(self, **kwargs):
        context = super(TagCreate, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('tags')
    template_name = 'tag_update.html'

    def get_context_data(self, **kwargs):
        context = super(TagUpdate, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tags')


# TaskStatus views
class TaskStatusesView(generic.ListView):
    template_name = 'task_statuses.html'
    context_object_name = 'task_statuses'

    def get_queryset(self):
        return TaskStatus.objects.all()


class TaskStatusView(generic.DetailView):
    model = TaskStatus
    template_name = "task_status.html"


class TaskStatusCreate(LoginRequiredMixin, CreateView):
    model = TaskStatus
    fields = '__all__'
    success_url = reverse_lazy('task_statuses')

    def get_context_data(self, **kwargs):
        context = super(TaskStatusCreate, self).get_context_data(**kwargs)
        context['task_statuses'] = TaskStatus.objects.all()
        return context


class TaskStatusUpdate(LoginRequiredMixin, UpdateView):
    model = TaskStatus
    fields = '__all__'
    success_url = reverse_lazy('task_statuses')
    template_name = 'taskstatus_update.html'

    def get_context_data(self, **kwargs):
        context = super(TaskStatusUpdate, self).get_context_data(**kwargs)
        context['task_statuses'] = TaskStatus.objects.all()
        return context


class TaskStatusDelete(LoginRequiredMixin, DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('task_statuses')
