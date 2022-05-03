from django.urls import path

from .views import ListUserFavoriteArticlesAPIView, FavoriteAPIView

urlpatterns = [
    path("articles/list/users/me/", ListUserFavoriteArticlesAPIView.as_view(),
         name="favorites-list-by-user-me"),
    path("articles/<slug:slug>/", FavoriteAPIView.as_view(),
         name="favorites-create"),
]
