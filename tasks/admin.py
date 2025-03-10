from django.contrib import admin
from .models import Task, TaskGroup


# Register your models here.
class TaskInline(admin.TabularInline):
    model = Task


class TaskGroupAdmin(admin.ModelAdmin):
    # This adds a table of all related Task objects
    inlines = [TaskInline,]


class TaskAdmin(admin.ModelAdmin):
    model = Task

    # Use the name to search
    search_fields = ('name', )

    # Display just the name and the due date in the list
    list_display = ('name', 'due_date',)

    # Enable filtering via the teacher's name and the number of units
    list_filter = ('due_date', )

    # Organizes the fields
    fieldsets = [
        # fieldsets is a list of tuples where the syntax is:
        # ('label of the field', {'fields': [<list of fields>]})
        ('Details', {
            'fields': [
                # the tuple puts these fields in a single line
                ('name', 'due_date'), 'taskgroup'
            ]
        }),
    ]


# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
#meow
admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)
