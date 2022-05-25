from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from accounts.models import CustomUser
from .serializers import UserSerializer


class ProfileView(DetailView, LoginRequiredMixin):
    model = CustomUser
    template_name = 'registration/profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class SignUpView(CreateView):
    success_url = reverse_lazy('login')
    form_class = UserSerializer
    template_name = 'registration/signup.html'
