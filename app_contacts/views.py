from django.shortcuts import render
from .models import Employees


def contacts_views(request):
    employees_list = Employees.objects.filter(id=6)
    employeer = Employees.objects.filter(id=5).last()
    context = {'employees_list': employees_list, 'title': 'Contacts', 'employeer': employeer}
    return render(request, 'contacts.html', context)


def contacts_detail_views(request, id):
    employees_list = Employees.objects.filter(id=id)
    employeer = Employees.objects.filter(id=id).last()
    context = {'employees_list': employees_list, 'title': 'Contacts', 'employeer': employeer}
    return render(request, 'contacts.html', context)