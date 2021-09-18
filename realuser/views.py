from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import sys
sys.path.append('../')
from users.models import *
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("realuser:login"))
    else:
        couseslist = []
        for c in Couses.objects.all():
            if request.user in c.nisit.all():
                couseslist.append(c)
        return render(request, "realuser/index.html",{
            "couseslist" : couseslist
        })

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("realuser:index"))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("realuser:index"))
        else:
            return render(request, "realuser/login.html", {"fail": "Invalid credential"})
    return render(request, "realuser/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "realuser/login.html", {
        "messages": messages.get_messages(request)
    })