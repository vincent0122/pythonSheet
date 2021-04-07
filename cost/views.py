from django.shortcuts import render, redirect, reverse
from .apps import update_cell
from users import models as user_models
import time

# Create your views here.


def cost_update(request):
    user = request.user
    when = time.strftime("%y-%m-%d %H:%M:%S")
    amount = request.GET.get("amount")
    detail = request.GET.get("detail")
    etc = request.GET.get("etc")

    user = user_models.User.objects.get(email=request.user).first_name

    update_cell(when, user, amount, detail, etc)
    return render(request, "cost/update.html")
