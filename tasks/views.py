from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task, TaskGroup


@login_required
def task_list(request):
    tasks = Task.objects.all()
    taskgroups = TaskGroup.objects.all()
    ctx = {"tasks": tasks, "taskgroups": taskgroups}
    if (request.method == "POST"):
        t = Task()
        t.name = request.POST.get('task_name')
        t.due_date = request.POST.get('task_due')
        t.taskgroup = TaskGroup.objects.get(pk=request.POST.get('taskgroup'))
        t.save()
        return render(request, 'task_list.html', ctx)
    else:
        return render(request, 'task_list.html', ctx)


@login_required
def task_detail(request, id):
    ctx = {'task': Task.objects.get(id=id)}
    return render(request, 'tasks/task_detail.html', ctx)
