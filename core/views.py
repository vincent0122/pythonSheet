# from django.shortcuts import render
# from . import airtable


# def list_issues(request):
#     page = request.GET.get("page")
#     issue_list = airtable.airtable_download()
#     paginator = Paginator(issue_list, 3)
#     issues = paginator.get_page(page)
#     return render(request, "issues/list.html", {"issues": issues})
