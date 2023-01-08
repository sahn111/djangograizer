from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect    
from django.urls import reverse

from .forms import StableForm
from .models import Stable

from cattle.models import Cattle
from cattle.forms import CattleForm

# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse("cattle:index"))

def save(request):
    if request.method == "POST":
        form = StableForm(request.POST)
        if form.is_valid():
            stable = Stable(name = form.cleaned_data['name'],
                            address = form.cleaned_data['address'],
                            capacity = form.cleaned_data['capacity']
            )
            stable.save()

    return HttpResponseRedirect(reverse("cattle:index"))

def get_stable(request, stable_id):

    stable = get_object_or_404(Stable, pk=stable_id)

    return render(request, "cattle:indexhtml", {
        "cattles" : Cattle.objects.all(),
        "stables" : Stable.objects.all(),
        "cattle_form" : CattleForm,
        "stable_form" : StableForm,
    })