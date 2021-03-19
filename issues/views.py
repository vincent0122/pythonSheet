# from django.shortcuts import render
# from django.http import HttpResponse


# def intro_issues(request):
#     return render(request, "issues/intro.html")
import os
from airtable import Airtable
from dotenv import load_dotenv
from django.shortcuts import render
from django.core.paginator import Paginator
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")
base_key = os.getenv("BASE_ID")
# from . import airtable


def list_issues(request):
    airtable = Airtable(base_key, "dataBase", api_key)
    print(vars(request))

    # url을 통해서 Name 숫자를 받고, 그것을 기반으로 record_id를 추출한다
    return render(request, "issues/list.html")