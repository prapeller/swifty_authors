from django.urls import path

from .views import CommentListCreateAPIView, CommentUpdateDeleteAPIView

urlpatterns = [
    path("article/<slug:article_slug>/", CommentListCreateAPIView.as_view(),
         name="comments-list-create"),
    path("<str:comment_id>/", CommentUpdateDeleteAPIView.as_view(),
         name="comments-update-delete"),
]
