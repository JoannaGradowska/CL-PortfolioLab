from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import SignUpForm


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/register.html', context={
            'form': form,
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('login')

        else:

            return render(request, 'registration/register.html', context={'form': form})
