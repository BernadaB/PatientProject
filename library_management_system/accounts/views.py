from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserCreationForm1
from accounts.models import CustomUser, Student


class SignUp(View):
    def post(self, request):
        form = CustomUserCreationForm(request)
        context = {'form': CustomUserCreationForm}
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        classroom = request.POST['classroom']
        if password != password_confirmation:
            pass_not_match = True
            return render(request, 'registration/signup.html', context)
        user = CustomUser.objects.create(email=email, user_type=1, name=name)
        student = Student.objects.create(user=user, classroom=classroom)
        user.save()
        student.save()
        return render(request, 'main/home.html', context=context)

    def get(self, request):
        return render(request, 'registration/signup.html', {'form': CustomUserCreationForm})


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile-detail.html'

    def get_object(self, **kwargs):
        return CustomUser.objects.get(id=self.kwargs['pk'])


class ProfileUpdateView(UpdateView):
    model = CustomUser
    template_name = 'accounts/profile-update.html'

    def get_object(self, **kwargs):
        return CustomUser.objects.get(id=self.kwargs['pk'])