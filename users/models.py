from django.contrib.auth.models import AbstractUser
from django.db import models


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
    avatar = models.ImageField(null=True, blank=True)
    license = models.TextField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
