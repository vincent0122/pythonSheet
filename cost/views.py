from django.shortcuts import render
from .apps import update_cell

# Create your views here.


def cost_update(request):
    update_cell()
    return render(request, "cost/update.html")
