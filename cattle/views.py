from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Cattle
from stable.models import Stable
from stable.forms import StableForm
from .forms import CattleForm, CattleStableFrom

def index(request):
    return render(request, "cattle/index.html",{
        "cattles" : Cattle.objects.all(),
        "stables" : Stable.objects.all(),
        "cattle_form" : CattleForm,
        "cattle_stable_form" : CattleStableFrom,
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

def get_stable(request):
    form = CattleStableFrom(request.GET)

    if form.is_valid():
        stable = form.cleaned_data['stable']
        return render(request, "cattle/index.html", {
            "cattles" : Cattle.objects.filter(Q(stable=stable)),
            "stables" : Stable.objects.all(),
            "cattle_form" : CattleForm,
            "cattle_stable_form" : CattleStableFrom,
            "stable_form" : StableForm,
        })

def get_weight(request):
    form = CattleForm(request.POST)
    if form.is_valid():
        weight = form.cleaned_data['weight']
        stable = form.cleaned_data['stable']

        return render(request, "cattle/index.html", {
            "cattles" : Cattle.objects.filter(Q(weight__gt=weight) & Q(stable=stable)),
            "stables" : Stable.objects.all(),
            "cattle_stable_form" : CattleStableFrom,
            "cattle_form" : CattleForm,
            "stable_form" : StableForm,
        })
            
            
