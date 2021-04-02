from django.urls import path
from . import views

app_name = "stocks"

urlpatterns = [
    path("stock_future/", views.stock_future, name="stock_future"),
]