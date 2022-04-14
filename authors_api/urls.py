from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

schema_view = get_schema_view(
    openapi.Info(title="Swifty Authors API",
                 default_version="v1",
                 description="API endpoints for Swifty Authors API",
                 contact=openapi.Contact(email="pavelmirosh@gmail.com"),
                 license=openapi.License(name="MIT")),
    permission_classes=(permissions.AllowAny,),
    public=True,
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
]
title = "Swifty Authors API Admin portal"
admin.site.site_header = admin.site.site_title = title
admin.site.index_title = _(f"Welcome to the {title}")
