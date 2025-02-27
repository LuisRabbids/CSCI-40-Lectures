from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', ctx)


def task_detail(request, id):
    ctx = {'task', Task.objects.get(id=id)}
    return render(request, 'task_detail.html', ctx)