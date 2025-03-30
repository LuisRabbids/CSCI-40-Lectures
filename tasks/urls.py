from django.urls import path
from .views import task_list, task_detail

urlpatterns = [
    path('', task_list, name="task-list"),  # /tasks/
    path('<int:id>/', task_detail, name='task-detail')
]

app_name = 'tasks'
#luis