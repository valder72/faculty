from django.contrib import admin

from .models import Department, Discipline, FacultyInfo, Program, Teacher, ExchangeProgram


# Register your models here.
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("name", "program")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")


@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ["university", "places", "deadline"]
