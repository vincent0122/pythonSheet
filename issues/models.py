from django.db import models
from core import models as core_models


class Issue(core_models.TimeStampedModel):

    """ Issue Model """

    attachment1 = models.ImageField(upload_to="images", blank=True)
    attachment2 = models.FileField(upload_to="files", blank=True)

    def __str__(self):
        return self.caption