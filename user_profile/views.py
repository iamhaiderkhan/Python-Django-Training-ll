from django.shortcuts import render
from django.views.generic import FormView, ListView, CreateView , UpdateView
from .forms import UserForm, UserProfileForm, UserUpdateForm
from .models import User, UserProfile
from django.http import HttpResponseRedirect
from django.core import serializers

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserForm
    second_form_class = UserProfileForm
    success_url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        context = dict()
        context['form1'] = self.form_class
        context['form2'] = self.second_form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            user_data = form.save()
            profile_data = form2.save(commit=False)
            profile_data.user = user_data
            profile_data.save()

            return HttpResponseRedirect(self.success_url)

        else:
            return render(request, self.template_name, {"form1": form, "form2": form2})


class HomeView(ListView):
    model = UserProfile
    template_name = "home.html"
    paginate_by = 50


class UserProfileUpdateView(UpdateView):
    model = User
    template_name = 'profile/profile-update.html'
    form_class = UserUpdateForm
    second_form_class = UserProfileForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        context = dict()
        super(UserProfileUpdateView, self).get(self, request, *args, **kwargs)
        context['form1'] = self.form_class(instance=request.user)
        context['form2'] = self.second_form_class(instance=request.user.profile)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        form2 = self.second_form_class(request.POST, instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            user_data = form.save()
            profile_data = form2.save(commit=False)
            profile_data.user = user_data
            profile_data.save()

            return HttpResponseRedirect(self.success_url)

        else:
            return render(request, self.template_name, {"form1": form, "form2": form2})