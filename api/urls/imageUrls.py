from django.conf.urls import url
from django.urls import path

from api import views
from api.views import imageViews

urlpatterns = [
    path('', imageViews.apiOverview, name="api-overview"),
    url(r'^upload', imageViews.ImageList.as_view()),
]