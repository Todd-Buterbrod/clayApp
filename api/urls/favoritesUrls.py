from django.urls import path
from api.views import favoritesViews

urlpatterns = [
    path('', favoritesViews.apiOverview, name="api-overview"),
    path('create/', favoritesViews.favoritesCreate, name="favorites-create"),
    path('delete/<str:pk>/', favoritesViews.favoritesDelete, name="favorites-delete"),
    path('list/', favoritesViews.favoritesList, name="favorites-list"),
    path('get/<str:pk>/', favoritesViews.favoritesGetById, name="favorites-get-by-id"),
]