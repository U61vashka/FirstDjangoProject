from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SimpleLoginView(LoginView):
    template_name = 'signin.html'


class SimpleSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('authentication:signin')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next')
        if next_url:
            self.success_url = next_url
        return response


class SimpleLogoutView(LogoutView):
    template_name = '/logged_out.html'
