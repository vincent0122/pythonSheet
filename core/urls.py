from django.urls import path
from issues import views as issue_views

app_name = "core"

urlpatterns = [
    path("", issue_views.CreateIssueView.as_view(), name="create"),
]