from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "first_name",
        "email",
        "position",
        "company",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
    list_filter = ("company", "working_place")
