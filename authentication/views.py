from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegister(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "register/register.html", {'form': form})


def login_session(request):
    if request.method == "GET":
        form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if(form.is_valid()):
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                for msg in form.error_messages:
                    messages.error(request, "Usuario no valido")
        else:
            for msg in form.error_messages:
                messages.error(request, "Información incorrecta")
                
    return render(request, "login/login.html", {'form':form})

def logout_session(request):
    logout(request)
    return redirect("home")