from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .forms import TaskForm
from .models import Task
from .paginations import SimplePagination
from .permissions import MustBeAuthorMixin, IsAuthorOrReadOnly
from .serializers import TaskSerializer


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


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = SimplePagination
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    pagination_class = SimplePagination
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)
