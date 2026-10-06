from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Department, FacultyInfo, Program, ExchangeProgram


# Create your views here.
def home(request):
    faculty = FacultyInfo.objects.first()
    return render(request, "home.html", {"faculty": faculty})


def program_list(request):
    programs = Program.objects.all()
    return render(request, "programs/list.html", {"programs": programs})


def program_detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, "programs/detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.prefetch_related("programs").all()
    return render(request, "departments/list.html", {"departments": departments})


def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    professors = department.teachers.all()
    return render(
        request,
        "departments/detail.html",
        {"department": department, "professors": professors},
    )

def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    today = date.today()
    return render(
        request, "exchange/list.html", {"programs": programs, "today": today}
    )

def exchange_detail(request, exchange_id):
    detail = get_object_or_404(ExchangeProgram, pk=exchange_id)
    today = date.today()
    return render(
        request,
        "exchange/detail.html",
        {"detail": detail, "item": detail, "today": today},
    )
