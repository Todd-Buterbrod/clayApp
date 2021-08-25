from django.urls import path
from api.views import followingViews

urlpatterns = [
    path('', followingViews.apiOverview, name="api-overview"),
    path('create/', followingViews.followingCreate, name="following-create"),
    path('delete/<str:pk>/', followingViews.followingDelete, name="following-delete"),
    path('list/', followingViews.followingList, name="following-list"),
    path('get/<str:pk>/', followingViews.followingGet, name="following-get"),
    path('get-by-followed-id/<str:pk>/', followingViews.followingGetByFollowedId, name="following-get-by-followed-id"),
    path('get-by-followers-id/<str:pk>/', followingViews.followingGetByFollowersId, name="following-get-by-followers-id"),
]