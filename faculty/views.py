from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("Home page")


def program_list(request):
  return HttpResponse("Programs list")


def program_detail(request, id):
  return HttpResponse(f"Program {id}")


def department_list(request):
  return HttpResponse("Departments list")


def department_detail(request, id):
  return HttpResponse(f"Department {id}")
