import os
from airtable import Airtable
from dotenv import load_dotenv
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from users import models as user_models
from . import models, forms
from datetime import datetime
from config.settings import DEBUG


load_dotenv()
api_key = os.getenv("API_KEY")
base_key = os.getenv("BASE_ID")
airtable = Airtable(base_key, "dataBase", api_key)
air_view = os.getenv("AIR_VIEW")

if DEBUG:
    root_url = "http://127.0.0.1:8000/"
else:
    root_url = "https://hpdjango.herokuapp.com/"


def intro(request):
    return render(request, "issues/intro.html")


def issue_create(request):
    user = request.user
    if request.method == "POST":
        form = forms.AddForm(request.POST)
        file_form = forms.FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist("첨부파일")
        if form.is_valid() and file_form.is_valid():
            issue_instance = form.save(commit=False)
            issue_instance.user = user
            issue_instance.save()
            for f in files:
                issuefile_instance = models.IssueFile(첨부파일=f, issue=issue_instance)
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
    print(name)
    if name == "임진석" or "심동현" or "임진아":
        team = "수출입"

    if name == "정소영" or "이선화" or "추승혜" or "송혜주":
        team = "총무"

    if name == "임진강" or "나준호":
        team = "영업"

    issue = request.POST.get("issue")
    customer = request.POST.get("customer")
    meeting = request.POST.get("meeting")
    ing = request.POST.get("ing")

    if meeting == "on":
        check = True
    else:
        check = False

    if ing == "on":
        check2 = True
    else:
        check2 = False

    files = models.IssueFile.objects.all()
    issues = models.Issue.objects.all()

    file_value = models.IssueFile.objects.values()
    file_urls = []
    today = datetime.today().strftime("%Y/%m/%d")

    for f in file_value:
        file_name = f["첨부파일"]
        file_url = dict(url=f"{root_url}media/{file_name}")
        file_urls.append(file_url)
    if issue:
        airtable.insert(
            {
                "부서": team,
                "날짜": today,
                "작성자": name,
                "거래처": customer,
                "내용": issue,
                "팀장회의": check,
                "진행중": check2,
                "Attachments": file_urls,
            }
        )

    # 에어테이블 업로드 후, 삭제
    files.delete()
    issues.delete()

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

    if data.get("팀장회의") is not None:
        check = data["팀장회의"]
    else:
        check = False

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
                "check": check,
            },
        )


def issue_edit(request):
    record = airtable.match("ID", request.GET.get("ID"))
    customer = request.GET.get("customer")
    detail = request.GET.get("detail")
    check = request.GET.get("check")
    if check == "on":
        check = True
    fields = {"내용": detail, "거래처": customer, "팀장회의": check}

    airtable.update(record["id"], fields)

    return redirect(reverse("core:home"))


def attachment_edit(request):
    user = request.user
    if request.method == "POST":
        form = forms.AddForm(request.POST)
        file_form = forms.FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist("첨부파일")
        if form.is_valid() and file_form.is_valid():
            issue_instance = form.save(commit=False)
            issue_instance.user = user
            issue_instance.save()
            for f in files:
                issuefile_instance = models.IssueFile(첨부파일=f, issue=issue_instance)
                issuefile_instance.save()
    else:
        form = forms.AddForm()
        file_form = forms.FileFieldForm()

    files = models.IssueFile.objects.all()
    issues = models.Issue.objects.all()
    file_value = models.IssueFile.objects.values()
    file_urls = []

    for f in file_value:
        file_name = f["첨부파일"]
        file_url = dict(url=f"{root_url}media/{file_name}")
        file_urls.append(file_url)

    ID = request.GET.get("ID", 0)
    record = airtable.match("ID", request.GET.get("ID"))

    if record["fields"].get("Attachments") is not None:
        data = record["fields"]["Attachments"]

    if len(list(files)) > 0:
        file_value = models.IssueFile.objects.values()
        file_urls = []

        for f in file_value:
            file_name = f["첨부파일"]
            file_url = dict(url=f"{root_url}media/{file_name}")
            file_urls.append(file_url)

        for urls in data:
            file_url = dict(url=urls["url"])
            file_urls.append(file_url)

        fields = {"Attachments": file_urls}
        airtable.update(record["id"], fields)
        print(fields)
        files.delete()
        issues.delete()

        return redirect(reverse("core:home"))

    else:
        number = 0
        attachments = []

        for attach in data:
            number = number + 1
            line = []
            line.append(number)
            line.append(attach["url"])
            line.append(attach["filename"])
            attachments.append(line)

        return render(
            request,
            "issues/attachments_edit.html",
            {"attachments": attachments, "ID": ID, "file_form": file_form},
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
    return redirect(reverse("core:home"))


def tlmeeting(request):
    datas = airtable.search("팀장회의", "1")
    return render(request, "issues/tlmeeting.html", {"datas": datas})


def myissue(request):
    datas = airtable.search("진행중", "1")
    user = request.user
    name = user.first_name

    if name == "진석" or "동현":
        team = "수출입"

    matches = filter(lambda el: el["fields"]["작성자"] == name, datas)
    team_issues = filter(
        lambda el: el["fields"]["부서"] == team and el["fields"]["작성자"] != name, datas
    )
    datas = filter(
        lambda el: el["fields"]["부서"] == team and el["fields"]["부서"] != team, datas
    )

    # matching_user = dict(filter(lambda el:))
    return render(
        request,
        "issues/myissue.html",
        {"matches": matches, "team_issues": team_issues, "datas": datas},
    )


def checkUncheck(request):  # 자꾸 순환된다..
    datas = airtable.search("팀장회의", "1")
    idon = request.GET.getlist("idon", None)
    ids = []

    for d in datas:
        ids.append(d["id"])

    for i in idon:
        ids.remove(i)

    fields = {"팀장회의": False}
    for i in ids:
        airtable.update(i, fields)

    return redirect(reverse("core:home"))


def checkUncheck_issue(request):  # 자꾸 순환된다..
    datas = airtable.search("진행중", "1")
    idon = request.GET.getlist("idon", None)
    ids = []

    for d in datas:
        ids.append(d["id"])

    for i in idon:
        ids.remove(i)

    fields = {"진행중": False}
    for i in ids:
        airtable.update(i, fields)

    return redirect(reverse("core:home"))


# # 첨부파일 수정하기
# # 삭제하기
# http://127.0.0.1:8000/media/files/Screen_Shot_2021-03-24_at_16.53.56_PM_DyeHxtJ.png