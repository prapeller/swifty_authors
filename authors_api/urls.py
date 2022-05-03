from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core_apps.search.urls import router as search_router

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
    path(settings.ADMIN_URL, admin.site.urls),

    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0),
         name="schema-redoc"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json"),

    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/reactions/", include("core_apps.reactions.urls")),
    path("api/v1/favorites/", include("core_apps.favorites.urls")),
    path("api/v1/comments/", include("core_apps.comments.urls")),

    path("api/v1/search/", include("core_apps.search.urls")),
    path("api/v1/search-router/", include(search_router.urls)),

]

title = "Swifty Authors API"
admin.site.site_title = admin.site.site_header = title
admin.site.index_title = _(f"Welcome to {title}")
