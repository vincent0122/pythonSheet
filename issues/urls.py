from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    # path("create/", views.CreateRoomView.as_view(), name="create"),
    # path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("edit/", views.edit, name="edit"),
    path("attachments_edit/", views.attachment_edit, name="attachments_edit"),
    path("attachments_del/", views.attachment_del, name="attachments_del")
    # path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    # path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
    # path(
    #     "<int:room_pk>/photos/<int:photo_pk>/delete/",
    #     views.delete_photo,
    #     name="delete-photo",
    # ),
    # path(
    #     "<int:room_pk>/photos/<int:photo_pk>/edit/",
    #     views.EditPhotoView.as_view(),
    #     name="edit-photo",
    # ),
    # path("search/", views.SearchView.as_view(), name="search"),
]