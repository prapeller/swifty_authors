from django.urls import path

from .views import CreateDeleteReacteAPIView

urlpatterns = [
    path("create-delete/article/<slug:slug>/", CreateDeleteReacteAPIView.as_view(),
         name="reactions-create-delete")
]
