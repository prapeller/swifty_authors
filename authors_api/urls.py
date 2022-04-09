from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

schema_view = get_schema_view(openapi.Info(title="Authors API",
                                           default_version="v1",
                                           description="API endpoints for Authors API course",
                                           contact=openapi.Contact(email="pavelmirosh@gmail.com"),
                                           license=openapi.License(name="MIT License")),
                              permission_classes=(permissions.AllowAny,),
                              public=True,
                              )

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]
title = "Swifty Authors API Admin portal"
admin.site.site_header = admin.site.site_title = title
admin.site.index_title = _(f"Welcome to the {title}")