from django.db import models
from users.models import User
from . import validators


class Issue(models.Model):

    """ Issue Model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=80, blank=True)

    # def __str__(self):
    #     return self


class IssueFile(models.Model):

    """ Issue File Model """

    첨부파일 = models.FileField(
        upload_to="files/", blank=True, validators=[validators.validate_file_size]
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)