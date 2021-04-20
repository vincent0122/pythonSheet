import os
import requests
import json
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from . import forms, models, apps
from django.shortcuts import render
from config.settings import DEBUG

# 로그인 할 때, access_token을 받는다. 클로져로 넘겨서 사용하는건 되는데
# 나는 다른 py파일인 issues.view.py에서 access_token을 인자로 받는 함수를 실행시켜야 한다.
# 로그인된 상태에서 access_token을 request로 받아봐야 되는데, 이게 가능한지 모르겠다.
# 로그인시 발급된 access_token을 따로 저장해두었다가 사용하는 법 (근데 이건 6시간후 expire됨)
# refresh token을 이용해서 계속 갱신해주는 법

if DEBUG:
    root_url = "http://127.0.0.1:8000/"
else:
    # root_url = "https://hpdjango.herokuapp.com/"
    root_url = "https://hpdjangostaging.herokuapp.com/"


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "Nicoas", "last_name": "Serr", "email": "itn@las.com"}

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do: add succes message
    except models.User.DoesNotExist:
        # to do: add error message
        pass
    return redirect(reverse("core:home"))


def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    redirect_uri = f"{root_url}users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=profile,account_email,talk_message"
    )


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        redirect_uri = f"{root_url}users/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )

        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email")
        if email is None:
            raise KakaoException()
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        try:
            user = models.User.objects.get(email=email)
            models.User.objects.filter(first_name=user.first_name).update(
                name=access_token
            )
            if user.login_method != models.User.LOGING_KAKAO:
                raise KakaoException()
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=models.User.LOGING_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avatar.save(
                    f"{nickname}-avatar",
                    ContentFile(photo_request.content),
                    save=True,
                )
        login(request, user)
        return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("users:login"))


def kakao_sending(request, data):
    access_token = request.user.name

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": f"Bearer {access_token}"}

    data = {
        "template_object": json.dumps(
            {
                "object_type": "text",
                "text": data,
                "link": {"web_url": "hpdjango.herokuapp.com"},
            }
        )
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    if response.json().get("result_code") == 0:
        print("메시지를 성공적으로 보냈습니다.")
        return redirect(reverse("core:home"))
    else:
        print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : " + str(response.json()))
        return redirect(reverse("core:home"))
