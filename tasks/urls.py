from django.urls import path
from .views import task_list, add_task, completed_tasks

urlpatterns = [
    path('', task_list, name="task-list"),  # /tasks/
]

app_name = 'tasks'
