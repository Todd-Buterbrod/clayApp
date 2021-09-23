from django.urls import path
from api.views import taskViews

urlpatterns = [
    path('', taskViews.apiOverview, name="api-overview"),
    path('create/', taskViews.taskCreate, name="task-create"),
    path('get/<str:pk>/', taskViews.taskGet, name="task-get"),
    path('get-detail/<str:pk>/', taskViews.taskGetDetail, name="task-get-detail"),
    path('update/<str:pk>/', taskViews.taskUpdate, name="task-update"),
    path('list/', taskViews.taskList, name="task-list"),
    path('list/<str:pk>/', taskViews.taskListByProfile, name="task-list-by-profile"),
    path('delete/<str:pk>/', taskViews.taskDelete, name="task-delete"),
    path('get-with-username/<str:pk>/', taskViews.taskGetWithUsername, name="task-get-with-username"),
    path('done/<str:pk>/', taskViews.taskDone, name="task-done"),
    path('rejected/<str:pk>/', taskViews.taskRejected, name="task-rejected")
]
