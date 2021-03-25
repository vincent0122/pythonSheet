import os
from airtable import Airtable
from dotenv import load_dotenv
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from users import models as user_models
from . import models, forms

import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")
base_key = os.getenv("BASE_ID")
airtable = Airtable(base_key, "dataBase", api_key)
air_view = os.getenv("AIR_VIEW")


def Add(request):
    if request.method == "POST":
        form = forms.AddForm(request.POST, request.FILES)
        print(request.FILES, "이건 리퀘스트")
        if form.is_valid():
            form.save()
            print(models.Issue.objects.all(), "이건 오브젝트 올")
            return redirect("/")
    else:
        form = forms.AddForm()
    return render(request, "issues/create.html", {"form": form})


def Add2(request):
    user = request.user
    if request.method == "POST":
        form = forms.AddForm(request.POST)
        file_form = forms.FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist("file")
        print(files)
        if form.is_valid() and file_form.is_valid():
            issue_instance = form.save(commit=False)
            issue_instance.user = user
            issue_instance.save()
            for f in files:
                issuefile_instance = models.IssueFile(file=f, issue=issue_instance)
                issuefile_instance.save()
    else:
        form = forms.AddForm()
        file_form = forms.FileFieldForm()

    return render(
        request, "issues/create2.html", {"form": form, "file_form": file_form}
    )


class FileFieldView(FormView):
    form_class = forms.FileFieldForm
    template_name = "issues/create2.html"  # Replace with your template.
    success_url = "/"  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist("file_field")

        if form.is_valid():
            for f in files:
                print("이건 F", f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# def issue_create(request):
#     user = user_models.User.objects.get(email=request.user)
#     name = user.first_name
#     issue = request.GET.get("issue")
#     customer = request.GET.get("customer")
#     attachment = request.GET.get("attachment")

#     form.save()
#     # airtable.insert(
#     #     {
#     #         "작성자": name,
#     #         "거래처": customer,
#     #         "내용": issue,
#     #         #       "Attachments": "attachment",
#     #     }
#     # )

#     return redirect(reverse("core:add"))


# def issue_import(request):
#     return render(request, "issues/issue_import.html", {"air_view": air_view})


# def id_import(request):
#     ID = request.GET.get("ID", 1)
#     data = airtable.search("ID", ID)[0]["fields"]
#     date = data["날짜"]
#     writer = data["작성자"]
#     customer = data["거래처"]
#     detail = data["내용"]
#     attachments = []

#     if data.get("Attachments") is not None:
#         for attach in data["Attachments"]:
#             line = []
#             line.append(attach["url"])
#             line.append(attach["filename"])
#             attachments.append(line)

#     if len(data) < 1:
#         return render(request, "issues/issue_import.html")

#     else:
#         return render(
#             request,
#             "issues/issue_import.html",
#             {
#                 "date": date,
#                 "writer": writer,
#                 "customer": customer,
#                 "detail": detail,
#                 "ID": ID,
#                 "attachments": attachments,
#                 "air_view": air_view,
#             },
#         )


# def issue_edit(request):
#     # record = airtable.match("ID", request.GET.get("ID"))
#     # customer = request.GET.get("customer")
#     # detail = request.GET.get("detail")
#     # fields = {"내용": detail, "거래처": customer}

#     # airtable.update(record["id"], fields)

#     return redirect(reverse("core:add"))


# def attachment_edit(request):
#     ID = request.GET.get("ID", 0)
#     data = airtable.search("ID", ID)[0]["fields"]
#     number = 0
#     attachments = []

#     for attach in data["Attachments"]:
#         number = number + 1
#         line = []
#         line.append(number)
#         line.append(attach["url"])
#         line.append(attach["filename"])
#         attachments.append(line)

#     return render(
#         request, "issues/attachments_edit.html", {"attachments": attachments, "ID": ID}
#     )


# def attachment_del(request):
#     number = int(request.GET.get("number", 1))
#     number = number - 1
#     ID = request.GET.get("ID", 1)
#     record = airtable.match("ID", request.GET.get("ID"))
#     attachments = record["fields"]["Attachments"]
#     del attachments[number]

#     fields = {"Attachments": attachments}

#     airtable.update(record["id"], fields)
#     return redirect(reverse("core:add"))


# # 첨부파일 수정하기
# # 삭제하기
