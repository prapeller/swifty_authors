from django.urls import path
from rest_framework import routers

from .views import SearchArticleViewSet

router = routers.DefaultRouter()

router.register("", SearchArticleViewSet, basename="search-article")

urlpatterns = [
    path("", SearchArticleViewSet.as_view({"get": "list"}), name="search-article")
]
