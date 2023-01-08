from django.shortcuts import render

from .models import Cattle

def index(request):
    return render(request, "cattle/index.html",{
        "cattles" : Cattle.objects.all()
    })