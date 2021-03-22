import os
from airtable import Airtable
from dotenv import load_dotenv
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")
base_key = os.getenv("BASE_ID")
airtable = Airtable(base_key, "dataBase", api_key)
air_view = os.getenv("AIR_VIEW")
# from . import airtable


def list_issues(request):
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
        return render(request, "issues/issue_list.html")

    else:
        return render(
            request,
            "issues/issue_list.html",
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


def edit(request):
    record = airtable.match("ID", request.GET.get("ID"))
    customer = request.GET.get("customer")
    detail = request.GET.get("detail")
    fields = {"내용": detail, "거래처": customer}

    airtable.update(record["id"], fields)
    return redirect(reverse("core:intro"))


def attachment_edit(request):
    ID = request.GET.get("ID", 1)
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
