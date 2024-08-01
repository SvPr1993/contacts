from django.contrib import admin
from .models import Employees


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'id')

#admin.site.register(Employees)