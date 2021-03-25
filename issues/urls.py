from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    path("add/", views.Add, name="add"),
    path("add2/", views.Add2, name="add2"),
    # path("issue_import/", views.issue_import, name="issue_import"),
    # path("id_import/", views.id_import, name="id_import"),
    # path("issue_edit/", views.issue_edit, name="issue_edit"),
    # path("issue_create/", views.issue_create, name="issue_create"),
    # path("attachments_edit/", views.attachment_edit, name="attachments_edit"),
    # path("attachments_del/", views.attachment_del, name="attachments_del"),
]