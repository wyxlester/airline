from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login required.")
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse("flights:index"))
            return HttpResponseRedirect(reverse("flights:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return render(request, "users/login.html")


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = forms.RegistrationForm()

    return render(request, 'users/register.html', {'form': form})
