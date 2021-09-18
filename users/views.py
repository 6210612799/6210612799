from django.http.response import HttpResponse, HttpResponseRedirect
import users 
from django.shortcuts import get_object_or_404, render 
from .models import Couses
from django.urls import reverse

# Create your views here.
def index(request):
    
    return render(request, "users/index.html",
    {
        "couses" : Couses.objects.all(),
        
    })
def do_couses(request , couses_id):
    
    couses = get_object_or_404(Couses, pk = couses_id)
        
    
    return render(request, "users/couses.html",{
        "couses" : couses,
        "portai" : couses.nisit.all(),
        "check"  : couses.is_full() ,
        "keekon" : couses.nisit.count(),
        

        
        
        
    })
def book(request, couses_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("realuser:login"))

    couses = get_object_or_404(Couses, pk = couses_id)
    if request.user not in couses.nisit.all():
        couses.nisit.add(request.user)
        couses.save()
    return HttpResponseRedirect(reverse("users:couses",args=(couses_id,)))

def debook(request, couses_id):
    couses = get_object_or_404(Couses, pk = couses_id)
    if request.user  in couses.nisit.all():
        couses.nisit.remove(request.user)
        couses.save()
    return HttpResponseRedirect(reverse("users:couses",args=(couses_id,)))

def admun(request, couses_id):
    if request.user.is_superuser:
        count = Couses.objects.get(id = couses_id)
        if count.status:
            count.status = False
            count.save()
        else:
            count.status = True
            count.save()
    return HttpResponseRedirect(reverse("users:couses", args=(couses_id,)))




