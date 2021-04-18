from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    path("issue_import/", views.issue_import, name="issue_import"),
    path("intro/", views.intro, name="intro"),
    path("id_import/", views.id_import, name="id_import"),
    path("id_comments/", views.id_comments, name="id_comments"),
    path("issue_edit/", views.issue_edit, name="issue_edit"),
    path("attachments_edit/", views.attachment_edit, name="attachments_edit"),
    path("attachments_del/", views.attachment_del, name="attachments_del"),
    path("tlmeeting/", views.tlmeeting, name="tlmeeting"),
    path("myissue/", views.myissue, name="myissue"),
    path("mypage/", views.mypage, name="mypage"),
    path("checkUncheck/", views.checkUncheck, name="checkUncheck"),
    path("checkUncheck_issue/", views.checkUncheck_issue, name="checkUncheck_issue"),
    path("delete/", views.delete, name="delete"),
]