from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import TaskForm
from .models import Task
from .permissions import MustBeAuthorMixin


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy('authentication:signin')
    success_url = reverse_lazy('tasks:task_list')

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Task()
        kwargs['instance'].creator = self.request.user
        return kwargs


class TaskUpdateView(LoginRequiredMixin, MustBeAuthorMixin, UpdateView):
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy('authentication:signin')
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(LoginRequiredMixin, MustBeAuthorMixin, DeleteView):
    model = Task
    login_url = reverse_lazy('authentication:signin')
    success_url = reverse_lazy('tasks:task_list')
