from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Cattle
from stable.models import Stable
from stable.forms import StableForm
from .forms import CattleForm

def index(request):
    return render(request, "cattle/index.html",{
        "cattles" : Cattle.objects.all(),
        "stables" : Stable.objects.all(),
        "cattle_form" : CattleForm,
        "stable_form" : StableForm,
    })

def create_item(request):
    if request.method == "POST":
        print("here")
        form = CattleForm(request.POST)
        if form.is_valid():
            cattle = Cattle(weight = form.cleaned_data['weight'], stable = form.cleaned_data['stable'])
            cattle.save()

    return HttpResponseRedirect(reverse("cattle:index"))

def read_item(request, item_id):
    item = get_object_or_404(Cattle, pk=item_id)
    return render(request, 'items/read_cattle.html', {'item': item})

def update_item(request, item_id):
    item = get_object_or_404(Cattle, pk=item_id)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.save()
    return render(request, 'items/update_cattle.html', {'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Cattle, pk=item_id)
    item.delete()
    return render(request, 'items/delete_cattle.html', {'item': item})

def get_cattle(request, cattle):
    return render(request, "cattle/cattle.html",{
        "cattle" : Cattle.objects.filter(id=cattle)
    })

def get_weight(request):
    form = CattleForm(request.POST)
    if form.is_valid():
        weight = form.cleaned_data['weight']
        stable = form.cleaned_data['stable']

        return render(request, "cattle/index.html", {
            "cattles" : Cattle.objects.filter(Q(weight__gt=weight) & Q(stable=stable)),
            "stables" : Stable.objects.all(),
            "cattle_form" : CattleForm,
            "stable_form" : StableForm,
        })
            
            
