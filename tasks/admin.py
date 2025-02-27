from django.contrib import admin
from .models import Task, TaskGroup


# Register your models here.
class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup


class TaskAdmin(admin.ModelAdmin):
    model = Task

    # Use the name to search
    search_fields = ('name', )

    # Display just the name and the due date in the list
    list_display = ('name', 'due_date',)
    
    # Enable filtering via the teacher's name and the number of units
    list_filter = ('due_date', )


# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)
