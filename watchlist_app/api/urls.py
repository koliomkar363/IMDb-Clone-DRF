from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api import views
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, WatchListGV, StreamPlatformVS, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, UserReview)

# Viewsets and Routers
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),

    # Viewsets and Routers
    path("", include(router.urls)),

    # path("stream/", StreamPlatformAV.as_view(), name="stream-list"),
    # path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="stream-detail"),

    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),

    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),

    # Filtering against the URL
    # path('reviews/<str:username>/', UserReview.as_view(), name="user-review-detail"),

    # Filtering against query parameters
    path('reviews/', UserReview.as_view(), name="user-review-detail"),
    path('list2/', WatchListGV.as_view(), name="watch-list"),
]

# urlpatterns = [
#     path("list/", views.movie_list, name="movie-list"),
#     path("<int:pk>/", views.movie_details, name="movie-details"),
# ]
