from django.urls import path
from .views import (
    ProfileListAPIView,
    ProfileDetailAPIView, UpdateProfileAPIView,
    FollowUnfollowAPIView, get_followers,
)

urlpatterns = [
    path("list/", ProfileListAPIView.as_view(), name="profiles-list"),
    path("detail/<str:username>/", ProfileDetailAPIView.as_view(), name="profiles-detail"),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name="profiles-update"),
    path("followers/<str:username>/", get_followers, name="profiles-followers"),
    path("follow-unfollow/<str:username>/", FollowUnfollowAPIView.as_view(), name="profiles-follow-unfollow"),
]
