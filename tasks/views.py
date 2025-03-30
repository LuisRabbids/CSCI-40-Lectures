from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TaskForm
from .models import Task, TaskGroup


@login_required
def task_list(request):
    tasks = Task.objects.all()
    taskgroups = TaskGroup.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            t = Task()
            t.name = form.cleaned_data.get('name')
            t.due_date = form.cleaned_data.get('due_date')
            t.taskgroup = form.cleaned_data.get('taskgroup')
            t.save()

    ctx = {"tasks": tasks, "taskgroups": taskgroups, "form": form}
    return render(request, 'tasks/task_list.html', ctx)


@login_required
def task_detail(request, id):
    ctx = {'task': Task.objects.get(id=id)}
    return render(request, 'tasks/task_detail.html', ctx)
