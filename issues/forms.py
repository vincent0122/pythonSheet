from django import forms
from . import models


class CreateForm(forms.Form):

    attachment1 = forms.ImageField(required=False)
    attachment2 = forms.FileField(required=False)

    def save(self):
        attachment1: self.cleaned_data.get("attachement1")
        attachment2: self.cleaned_data.get("attachement2")

        issue = models.Issue.objects.create(attachment1, attachment2)
        issue.save()
