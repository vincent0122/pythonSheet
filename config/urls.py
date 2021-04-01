from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # 파일들을 제공하는 역할을 함
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("issues/", include("issues.urls", namespace="issues")),
    path("stocks/", include("stocks.urls", namespace="urls")),
    path("admin/", admin.site.urls),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
