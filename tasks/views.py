from django.shortcuts import render

# Create your views here.


def task_list(request):
    ctx = {
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }
    return render(request, "tasks/task_list.html", ctx)


def add_task(request):
    return render(request, "tasks/add_task.html")


def completed_tasks(request):
    ctx = {"completed_tasks": ["Submit report", "Attend meeting"]}
    return render(request, "tasks/completed_tasks.html", ctx)
