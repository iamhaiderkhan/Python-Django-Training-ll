from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import SignUpForm
from .models import UserProfile, User


class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = '/auth/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class HomeView(ListView):
    model = UserProfile
    template_name = "home.html"
    paginate_by = 50
