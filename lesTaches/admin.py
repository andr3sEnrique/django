from django.contrib import admin
from lesTaches.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','created_date', 'colored_due_date')
    read_only=('created_date')


admin.site.register(Task,TaskAdmin)

# Register your models here.
