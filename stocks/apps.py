from django.apps import AppConfig
from core.google_auth import get_google

from backdata import base
import pandas as pd

from datetime import timedelta
from datetime import datetime as dt

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# import plotly.express as px
# from plotly import graph_objs as go
# from plotly.graph_objs import *

# import json

basic_setting = base.basic_setting


class StocksConfig(AppConfig):
    name = "stocks"


def get_sheetsId():
    gsheets_ids = {
        "factory_report": "1owxqOWAI_A31eDKafUDKfehy9gfSkPZT5dECwxqeihU",  # 공장일지
        "eta_status": "1_0DwnDGTJm6iKEYZHwVC9mDsvIQSq_7AWTG7pckeaow",  # eta현황
        "sales_status": "1U4pgA9tfj2sciXj_6LMQ74Vff81OButlpOBb_RVvH9c",  # 판매관리대장2021
    }

    return gsheets_ids


def get_sheet():  # gs 밑에다가
    gc = get_google()
    gs = get_sheetsId()
    result = {
        "stock": gc.open_by_key(gs["factory_report"]).worksheet("재고현황"),
        "actual_use_thisyear": gc.open_by_key(gs["factory_report"]).worksheet("원료제품누적"),
        "actual_use_lastyear": gc.open_by_key(gs["factory_report"]).worksheet("2020"),
        "sales21": gc.open_by_key(gs["sales_status"]).worksheet("2021"),
        "sales20": gc.open_by_key(gs["sales_status"]).worksheet("2020"),
        "eta": gc.open_by_key(gs["eta_status"]).worksheet("ETA현황"),
    }
    return result


def get_sheet_values():
    result = get_sheet()
    range = {
        "stock": "a3:g100",
        "actual_use_thisyear": "a1:e6000",
        "actual_use_lastyear": "a1:e6000",
        "sales21": "a1:n4000",
        "sales20": "a1:n4000",
        "eta": "a1:aa100",
    }
    values = {}
    values_df = {}
    header = {}

    for key in result.keys():
        values[key] = result[key].get(range[key])
        header[key] = values[key].pop(0)
        values_df[key] = pd.DataFrame(values[key], columns=header[key])

    return values_df


def date_setting():
    period = basic_setting["period_to_check"]
    date_data = {
        "last": dt.today() + timedelta(period),
        "tod": dt.today(),
        "yesterday": dt.today() - timedelta(1),
        "tod_month": dt.today().month,
        "tod_year": dt.today().year,
        "todPlus": dt.today() + timedelta(2),
        "last_start": "2020-01-01",
    }

    date_data["yesterday"] = date_data["yesterday"].strftime("%Y-%m-%d")
    date_data["history_start"] = (date_data["tod"] - timedelta(90)).strftime("%Y-%m-%d")

    return date_data


def cleaning_datas():
    items = basic_setting["items"]
    period = basic_setting["period_to_check"]
    date_data = date_setting()
    values_df = get_sheet_values()
    # values_df['stock'] = values_df['stock'].drop(
    #    [values_df['stock'].index[0], values_df['stock'].index[1]])

    def change_comma_to_float(key, col_name):
        values_df[key].loc[:, col_name] = values_df[key][col_name].str.replace(",", "")
        values_df[key].loc[:, col_name] = values_df[key][col_name].astype(float)
        return values_df

    values_df["stock2"] = values_df["stock"].iloc[:, [0, 2]]  # 원료 현재고 가져오기
    values_df["stock2"].columns = ["제품명", "수량"]
    values_df["stock3"] = values_df["stock"].iloc[:, [4, 6]]  # 제품 현재고 가져오기
    values_df["stock3"].columns = ["제품명", "수량"]
    values_df["stock"] = values_df["stock2"].append(values_df["stock3"])  # 두개 합치기
    values_df["stock"].columns = ["제품명", "수량"]
    values_df["stock"] = values_df["stock"][
        values_df["stock"]["제품명"].isin(items)
    ]  # 빈행 삭제
    values_df["stock"]["Date"] = date_data["tod"]  # 오늘 날짜 추가하기
    del values_df["stock2"]  # 기존 변수 삭제
    del values_df["stock3"]  # 기존 변수 삭제

    values_df["actual_use"] = pd.concat(  # 원료제품누적 올해, 작년 합치기
        [
            values_df["actual_use_thisyear"].iloc[:, [0, 2, 4]],
            values_df["actual_use_lastyear"].iloc[:, [0, 2, 4]],
        ]
    )
    del values_df["actual_use_thisyear"]
    del values_df["actual_use_lastyear"]

    values_df["sales21"] = values_df["sales21"][values_df["sales21"]["제품"] != ""]
    values_df["sales20"] = values_df["sales20"][values_df["sales20"]["제품"] != ""]
    change_comma_to_float("sales21", "수량")
    change_comma_to_float("sales21", "금액")
    change_comma_to_float("sales20", "수량")
    change_comma_to_float("sales20", "금액")
    change_comma_to_float("stock", "수량")

    values_df["eta"] = values_df["eta"].iloc[:, [0, 5, 6, 16, 17]]  # 16,17은 etd,eta
    values_df["eta"] = values_df["eta"][values_df["eta"].ETA != ""]
    values_df["eta"] = values_df["eta"][values_df["eta"].수입자 != "대한산업"]
    values_df["eta"].loc[:, "계약수량"] = values_df["eta"].계약수량.astype(float)
    values_df["eta"].계약수량 = values_df["eta"].계약수량 * 1000

    if (
        date_data["tod_month"] < 10
    ):  # 10월 이전꺼는 21년도라고 표시를 해주어야 함, 10월 넘어가면, 1,2,3월은 다음년도로 표시해주어야 함

        this_year = str(date_data["tod_year"])
        this_year = "/" + this_year[2:4]

        next_year = str(date_data["tod_year"] + 1)
        next_year = "/" + next_year[2:4]

        values_df["eta"]["ETA"] = values_df["eta"]["ETA"] + this_year
    else:
        values_df["eta"]["ETA"] = values_df["eta"]["ETA"].mask(
            values_df["eta"]["ETA"].dt.month == 1, values_df["eta"]["ETA"] + next_year
        )
        values_df["eta"]["ETA"] = values_df["eta"]["ETA"].mask(
            values_df["eta"]["ETA"].dt.month == 2, values_df["eta"]["ETA"] + next_year
        )
        values_df["eta"]["ETA"] = values_df["eta"]["ETA"].mask(
            values_df["eta"]["ETA"].dt.month == 3, values_df["eta"]["ETA"] + next_year
        )

    values_df["eta"]["ETA"] = pd.to_datetime(values_df["eta"]["ETA"], format="%m/%d/%y")

    values_df["eta"]["ETA"] = values_df["eta"]["ETA"] + timedelta(
        7
    )  # ETA +7일 후 입고된다고 가정
    values_df["eta"] = values_df["eta"][
        pd.to_datetime(values_df["eta"].ETA, errors="coerce") <= date_data["last"]
    ]
    values_df["eta"] = values_df["eta"][values_df["eta"].입고상태 != "완"]
    values_df["eta"]["ETA"].mask(
        values_df["eta"]["입고상태"] == "준", date_data["todPlus"], inplace=True
    )
    values_df["eta"]["ETA"].mask(
        values_df["eta"]["ETA"] <= date_data["tod"], date_data["todPlus"], inplace=True
    )
    values_df["eta"] = values_df["eta"].rename(
        {"ETA": "Date", "계약수량": "수량"}, axis="columns"
    )
    values_df["eta"] = values_df["eta"].iloc[:, [1, 2, 3]]

    values_df["fixed_df"] = values_df["stock"].append(values_df["eta"])
    values_df["fixed_df"] = values_df["fixed_df"][["Date", "제품명", "수량"]]
    values_df["fixed_df"]["Date"] = values_df["fixed_df"]["Date"].dt.strftime(
        "%y/%m/%d"
    )

    dataRange = []
    for i in range(0, period + 1):
        a = dt.today() + timedelta(i)
        a = dt.strftime(a, "%y/%m/%d")
        dataRange.append(a)

    values_df["actual_use"] = values_df["actual_use"][
        values_df["actual_use"].iloc[:, 2] != ""
    ]
    values_df["actual_use"] = values_df["actual_use"][
        values_df["actual_use"].iloc[:, 1].isin(items)
    ]
    values_df["actual_use"]["날짜"] = pd.to_datetime(
        values_df["actual_use"]["날짜"], format="%Y. %m. %d"
    )
    values_df["actual_use"]["날짜"] = values_df["actual_use"]["날짜"].dt.strftime(
        "%y/%m/%d"
    )
    values_df["actual_use"]["사용/출고"] = values_df["actual_use"]["사용/출고"].str.replace(
        ",", ""
    )
    values_df["actual_use"]["사용/출고"] = values_df["actual_use"]["사용/출고"].astype(float)

    a = pd.date_range(start=date_data["last_start"], end=dt.today() - timedelta(1))
    a = a.strftime("%y/%m/%d")
    b = values_df["stock"]["제품명"]
    raw_df = pd.DataFrame(index=a, columns=b)
    raw_df = raw_df.fillna(0)

    # 피벗 전까지 데이터 가공 --종료
    values_df["fixed_df"] = values_df["fixed_df"].pivot_table(
        index="Date", columns="제품명", values="수량", aggfunc="sum"
    )
    values_df["fixed_df"].index.name = None
    values_df["fixed_df"].columns.name = ""
    values_df["fixed_df"] = values_df["fixed_df"].fillna(0)
    values_df["fixed2_df"] = pd.DataFrame(
        columns=values_df["fixed_df"].columns, index=dataRange
    )
    values_df["fixed2_df"].index.name = None
    values_df["fixed2_df"].columns.name = ""
    values_df["fixed2_df"] = values_df["fixed2_df"].fillna(0)
    values_df["fixed_df"] = values_df["fixed_df"].add(values_df["fixed2_df"])
    values_df["fixed_df"] = values_df["fixed_df"].fillna(0)
    values_df["fixed_df"] = values_df["fixed_df"][items]
    del values_df["fixed2_df"]

    for i in range(1, period + 1):  # 누적데이터로 변경
        values_df["fixed_df"].iloc[i] = (
            values_df["fixed_df"].iloc[i - 1] + values_df["fixed_df"].iloc[i]
        )

    values_df["actual_use"] = values_df["actual_use"].pivot_table(
        index="날짜", columns="제품명", values="사용/출고", aggfunc="sum"
    )
    values_df["actual_use"] = values_df["actual_use"].fillna(0)
    values_df["actual_use"].index.name = None
    values_df["actual_use"].columns.name = ""
    raw_df.columns.name = ""
    values_df["actual_use"] = raw_df.add(values_df["actual_use"], fill_value=0)

    del values_df["stock"]
    del values_df["sales21"]
    del values_df["sales20"]
    del values_df["eta"]
    # 안쓸거 삭제

    return values_df


def making_graph(values_df, start, last, wv):
    datedata = date_setting()

    def set_stock_graph_color(x):
        if x < 0:
            return "#d3705a"
        else:
            return "#00754a"

    def get_mean():
        values_df["actual_use"].index = pd.to_datetime(
            values_df["actual_use"].index, format="%y/%m/%d"
        )
        lately = values_df["actual_use"].loc[start:last]
        sorter = basic_setting["items"]
        lately2 = pd.DataFrame(columns=sorter)
        lately = pd.concat([lately2, lately])  # 컬럼 순서를 맞추기 위해 새로 만들고, concat

        lately.index = lately.index.strftime("%y/%m/%d")
        b = round(lately.mean())
        lately = b * wv

        fig = update_graph(lately)

        return fig

    def update_graph(lately):
        values_df["final_his_df"] = values_df["fixed_df"].copy()

        for i in range(1, len(values_df["fixed_df"])):
            values_df["final_his_df"].iloc[i] = (
                values_df["fixed_df"].iloc[i] - lately * i
            )

        a = values_df["final_his_df"].columns.tolist()
        itemNum = len(values_df["final_his_df"].columns) / 3
        itemNum = int(itemNum)
        k = 0

        fig = make_subplots(
            rows=itemNum + 1,
            cols=3,
            shared_xaxes=True,
            subplot_titles=a,
            vertical_spacing=0.03,
            horizontal_spacing=0.05,
        )

        for i in range(1, itemNum + 2):
            for j in range(1, 4):
                fig.add_trace(
                    go.Scatter(
                        x=values_df["final_his_df"].index,
                        y=values_df["final_his_df"].iloc[:, k],
                        mode="lines+markers",
                        marker=dict(
                            size=3,
                            color=list(
                                map(
                                    set_stock_graph_color,
                                    values_df["final_his_df"].iloc[:, k],
                                )
                            ),
                        ),
                        line=dict(color="#00754a"),
                    ),
                    row=i,
                    col=j,
                )

                k = k + 1
                if k == len(values_df["final_his_df"].columns):
                    break

        for l in fig["layout"]["annotations"]:
            l["font"]["size"] = 10

        fig.update_layout(
            height=1800,
            showlegend=False,
            # paper_bgcolor="#f2f0eb",
            # plot_bgcolor="#f2f0eb",
        )
        fig.update_yaxes(
            zeroline=False, showgrid=True, gridwidth=1, gridcolor="lightgray"
        )
        fig.update_xaxes(zeroline=False, showgrid=False, showticklabels=False)

        return fig

    fig = get_mean()
    return fig
