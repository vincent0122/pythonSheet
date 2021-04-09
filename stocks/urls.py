from django.urls import path
from . import views

app_name = "stocks"

urlpatterns = [
    path("stock_future/", views.stock_future, name="stock_future"),
    path("stock_item/", views.stock_item, name="stock_item"),
]