from django.urls import path
from api.views import profileViews

urlpatterns = [
    path('', profileViews.apiOverview, name="api-overview"),
    path('create/', profileViews.profileCreate, name="profile-create"),
    path('list/', profileViews.profileList, name="profile-list"),
    path('get/<str:pk>/', profileViews.profileGet, name="profile-get"),
    path('update/<str:pk>/', profileViews.profileUpdate, name="profile-update"),
]