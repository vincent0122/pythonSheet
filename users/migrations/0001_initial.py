# Generated by Django 3.1.7 on 2021-04-06 05:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "company",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("(주)한펠", "(주)한펠"),
                            ("허니텍", "허니텍"),
                            ("(주)허니텍", "(주)허니텍"),
                            ("대한산업", "대한산업"),
                            ("기타", "기타"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("사장", "사장"),
                            ("상무", "상무"),
                            ("부장", "부장"),
                            ("차장", "차장"),
                            ("과장", "과장"),
                            ("대리", "대리"),
                            ("주임", "주임"),
                            ("사원", "사원"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "working_place",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("안양", "안양"),
                            ("발산리 구공장", "발산리 구공장"),
                            ("발산리 신공장", "발산리 신공장"),
                            ("장산리", "장산리"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars"),
                ),
                ("license", models.TextField(blank=True, null=True)),
                ("children", models.IntegerField(blank=True, null=True)),
                ("birthday", models.DateField(blank=True, null=True)),
                ("superhost", models.BooleanField(default=False)),
                ("email_verified", models.BooleanField(default=False)),
                (
                    "email_secret",
                    models.CharField(blank=True, default="", max_length=20),
                ),
                (
                    "login_method",
                    models.CharField(
                        choices=[
                            ("email", "Email"),
                            ("github", "Github"),
                            ("kakao", "Kakao"),
                        ],
                        default="email",
                        max_length=50,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
