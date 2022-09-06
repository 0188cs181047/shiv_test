from django.contrib import admin

# Register your models here.
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename','esal','eaddre']
    # ordering = ['']
    # actions = [make_published]

admin.site.register(Employee, EmployeeAdmin)
