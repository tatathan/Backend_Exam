from django.contrib import admin
from .models import School, Classroom, Teacher, Student
from .admin_forms import TeacherAdminForm, StudentAdminForm

admin.site.register(School)
admin.site.register(Classroom)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm
    list_display = ['first_name', 'last_name', 'sex', 'school']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ['first_name', 'last_name', 'sex', 'school']