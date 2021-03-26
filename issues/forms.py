from django import forms
from . import models


class AddForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = ["text"]


class FileFieldForm(forms.ModelForm):
    class Meta:
        model = models.IssueFile
        fields = ["첨부파일"]
        widgets = {
            "첨부파일": forms.ClearableFileInput(attrs={"multiple": True}),
        }
