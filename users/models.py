import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


class User(AbstractUser):

    """ Custom User Model """

    COMPANY_HANPEL = "(주)한펠"
    COMPANY_HONEY = "허니텍"
    COMPANY_HONEY2 = "(주)허니텍"
    COMPANY_DAEHAN = "대한산업"
    COMPANY_ETC = "기타"

    COMPANY_CHOICES = (
        (COMPANY_HANPEL, "(주)한펠"),
        (COMPANY_HONEY, "허니텍"),
        (COMPANY_HONEY2, "(주)허니텍"),
        (COMPANY_DAEHAN, "대한산업"),
        (COMPANY_ETC, "기타"),
    )

    POSITION_사장 = "사장"
    POSITION_상무 = "상무"
    POSITION_부장 = "부장"
    POSITION_차장 = "차장"
    POSITION_과장 = "과장"
    POSITION_대리 = "대리"
    POSITION_주임 = "주임"
    POSITION_사원 = "사원"

    POSITION_CHOICES = (
        (POSITION_사장, "사장"),
        (POSITION_상무, "상무"),
        (POSITION_부장, "부장"),
        (POSITION_차장, "차장"),
        (POSITION_과장, "과장"),
        (POSITION_대리, "대리"),
        (POSITION_주임, "주임"),
        (POSITION_사원, "사원"),
    )

    WP_안양 = "안양"
    WP_발산1 = "발산리 구공장"
    WP_발산2 = "발산리 신공장"
    WP_장산 = "장산리"

    WP_CHOICES = (
        (WP_안양, "안양"),
        (WP_발산1, "발산리 구공장"),
        (WP_발산2, "발산리 신공장"),
        (WP_장산, "장산리"),
    )  # WP는 Working Place

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )

    company = models.CharField(
        choices=COMPANY_CHOICES, max_length=10, null=True, blank=True
    )
    name = models.CharField(max_length=10, null=True, blank=True)
    position = models.CharField(
        choices=POSITION_CHOICES, max_length=10, null=True, blank=True
    )
    working_place = models.CharField(
        choices=WP_CHOICES, max_length=10, null=True, blank=True
    )
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    license = models.TextField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()

        return