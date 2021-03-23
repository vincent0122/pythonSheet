from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    path("create/", views.CreateIssueView.as_view(), name="create"),
    # path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("issue_import/", views.issue_import, name="issue_import"),
    path("id_import/", views.id_import, name="id_import"),
    path("issue_edit/", views.issue_edit, name="issue_edit"),
    path("issue_create/", views.issue_create, name="issue_create"),
    path("attachments_edit/", views.attachment_edit, name="attachments_edit"),
    path("attachments_del/", views.attachment_del, name="attachments_del"),
    # path("issue_update/", views.UpdateIssueView.as_view(), name="update"),
]