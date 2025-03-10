from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', ctx)


@login_required
def task_detail(request, id):
    ctx = {'task': Task.objects.get(id=id)}
    return render(request, 'tasks/task_detail.html', ctx)
