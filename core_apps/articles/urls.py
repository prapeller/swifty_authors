from django.urls import path

from .views import (
    ArticleCreateAPIView,
    ArticleDeleteAPIView,
    ArticleDetailView,
    ArticleListAPIView,
    update_article_api_view,
)

urlpatterns = [
    path("list/", ArticleListAPIView.as_view(), name="articles-list"),
    path("create/", ArticleCreateAPIView.as_view(), name="articles-create"),
    path("detail/<slug:slug>/", ArticleDetailView.as_view(), name="articles-detail"),
    path("update/<slug:slug>/", update_article_api_view, name="articles-update"),
    path("delete/<slug:slug>/", ArticleDeleteAPIView.as_view(), name="articles-delete"),
]
