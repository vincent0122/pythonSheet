from django.urls import path
from . import views

app_name = "cost"

urlpatterns = [
    path("cost_update/", views.cost_update, name="cost_update"),
]