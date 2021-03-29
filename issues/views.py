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


def intro(request):
    return render(request, "issues/intro.html")


def issue_create(request):
    user = request.user
    if request.method == "POST":
        form = forms.AddForm(request.POST)
        file_form = forms.FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist("file")
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

    try:
        user = user_models.User.objects.get(email=request.user)
    except:
        # raise ValueError("Please login with Kakao")
        return redirect(reverse("issues:intro"))

    name = user.first_name
    issue = request.POST.get("issue")
    print(issue)
    customer = request.POST.get("customer")

    files = models.IssueFile.objects.all()
    issues = models.Issue.objects.all()
    files.delete()
    issues.delete()

    # # os.rmdir(file_path)

    file_value = models.IssueFile.objects.values()
    file_urls = []

    for f in file_value:
        file_name = f["첨부파일"]
        file_url = (
            "url" f"https://hpdjango.herokuapp.com/media{file_name}"
        )  # deploy 이후 정리하면 됨
        file_urls.append(file_url)

    print(file_urls)

    airtable.insert(
        {
            "작성자": name,
            "거래처": customer,
            "내용": file_urls,
            # "Attachments": [
            #     {
            #         "url": "https://2.bp.blogspot.com/-aaYab7phjF4/Xa_TOXvC5hI/AAAAAAAAQME/2xf9AYY0450n-hAobHdEHRrYmPbcy0jsACLcBGAsYHQ/w914-h514-p-k-no-nu/suzy-beautiful-korean-girl-uhdpaper.com-4K-4.1423-wp.thumbnail.jpg"
            #     },
            #     {
            #         "url": "https://dl.airtable.com/.attachments/9d020ee5ca79c9b527c030ced8d83bef/0d11df0c/KakaoTalk_20200527_084727449.png",
            #     },
            # ],
        }
    )

    # 에어테이블 업로드 후, 삭제

    return render(request, "issues/issue_create.html", {"file_form": file_form})


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
    record = airtable.match("ID", request.GET.get("ID"))
    customer = request.GET.get("customer")
    detail = request.GET.get("detail")
    fields = {"내용": detail, "거래처": customer}

    airtable.update(record["id"], fields)

    return redirect(reverse("core:home"))


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
    return redirect(reverse("core:add"))


# # 첨부파일 수정하기
# # 삭제하기
# http://127.0.0.1:8000/media/files/Screen_Shot_2021-03-24_at_16.53.56_PM_DyeHxtJ.png