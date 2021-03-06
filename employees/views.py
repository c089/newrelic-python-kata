from .models import Employee, BioData, Payroll
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def list(request):
    employees = Employee.objects.all().prefetch_related('biodata', 'payroll')[:50]
    return render(request, 'employees/list.html', {'employees': employees})

def filtering(request):
    employees = Employee.objects.filter(name__startswith='X')
    return render(request, 'employees/filtering.html', {'employees': employees})
