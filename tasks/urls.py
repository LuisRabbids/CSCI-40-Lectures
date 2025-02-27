from django.urls import path
from .views import task_list, add_task, completed_tasks

urlpatterns = [
    path('', task_list, name="task-list"),  # /tasks/
    path('add/', add_task, name="add-task"),  # /tasks/add/
    path('completed/', completed_tasks,
         name="completed-tasks"),  # /tasks/completed/
]

app_name = 'tasks'
