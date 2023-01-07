from django.urls import path
from . import views


urlpatterns = [
    path("", views.api_routes),
    path("tasks/", views.TaskListCreate.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", views.TaskUpdateDelete.as_view(), name="task-detail")
]
