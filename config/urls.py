from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # 파일들을 제공하는 역할을 함


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("issues/", include("issues.urls", namespace="issues")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)