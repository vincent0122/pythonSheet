import os
from airtable import Airtable
from dotenv import load_dotenv
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from users import models as user_models
from . import forms

import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")
base_key = os.getenv("BASE_ID")
airtable = Airtable(base_key, "dataBase", api_key)
air_view = os.getenv("AIR_VIEW")


class CreateIssueView(FormView):

    print("1번 진행")
    template_name = "issues/create.html"
    form_class = forms.CreateForm
    success_url = reverse_lazy("www.naver.com")

    fields = (
        "temporary_image",
        "temporary_file",
    )

    # form.save()


def issue_create(request):
    user = user_models.User.objects.get(email=request.user)
    name = user.first_name
    issue = request.GET.get("issue")
    customer = request.GET.get("customer")
    attachment = request.GET.get("attachment")

    form.save()
    # airtable.insert(
    #     {
    #         "작성자": name,
    #         "거래처": customer,
    #         "내용": issue,
    #         #       "Attachments": "attachment",
    #     }
    # )

    return redirect(reverse("core:create"))


def issue_import(request):
    return render(request, "issues/issue_import.html", {"air_view": air_view})


def id_import(request):
    ID = request.GET.get("ID", 1)
    data = airtable.search("ID", ID)[0]["fields"]
    date = data["날짜"]
    writer = data["작성자"]
    customer = data["거래처"]
    detail = data["내용"]
    attachments = []

    if data.get("Attachments") is not None:
        for attach in data["Attachments"]:
            line = []
            line.append(attach["url"])
            line.append(attach["filename"])
            attachments.append(line)

    if len(data) < 1:
        return render(request, "issues/issue_import.html")

    else:
        return render(
            request,
            "issues/issue_import.html",
            {
                "date": date,
                "writer": writer,
                "customer": customer,
                "detail": detail,
                "ID": ID,
                "attachments": attachments,
                "air_view": air_view,
            },
        )


def issue_edit(request):
    # record = airtable.match("ID", request.GET.get("ID"))
    # customer = request.GET.get("customer")
    # detail = request.GET.get("detail")
    # fields = {"내용": detail, "거래처": customer}

    # airtable.update(record["id"], fields)

    return redirect(reverse("core:create"))


def attachment_edit(request):
    ID = request.GET.get("ID", 0)
    data = airtable.search("ID", ID)[0]["fields"]
    number = 0
    attachments = []

    for attach in data["Attachments"]:
        number = number + 1
        line = []
        line.append(number)
        line.append(attach["url"])
        line.append(attach["filename"])
        attachments.append(line)

    return render(
        request, "issues/attachments_edit.html", {"attachments": attachments, "ID": ID}
    )


def attachment_del(request):
    number = int(request.GET.get("number", 1))
    number = number - 1
    ID = request.GET.get("ID", 1)
    record = airtable.match("ID", request.GET.get("ID"))
    attachments = record["fields"]["Attachments"]
    del attachments[number]

    fields = {"Attachments": attachments}

    airtable.update(record["id"], fields)
    return redirect(reverse("core:intro"))


# 첨부파일 수정하기
# 삭제하기
