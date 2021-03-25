from django.db import models
from core import models as core_models
from users.models import User


class Issue(models.Model):

    """ Issue Model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=80, blank=True)

    # def __str__(self):
    #     return self


class IssueFile(models.Model):

    """ Issue File Model """

    file = models.FileField(upload_to="files/", blank=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.caption