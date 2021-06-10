from django.shortcuts import render, redirect
from .models import Employee, City
from .forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def employee(request):
    context = {}
    if request.POST:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pan_number = form.cleaned_data['pan_number']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            city = form.cleaned_data['city']
            gender = form.cleaned_data['gender']
            qs_add = Employee(name=name, pan_number=pan_number, email=email, age=age, city=city, gender=gender)
            qs_add.save()
            messages.add_message(request, messages.INFO, 'Employee save successfully')
            context['form'] = context['form'] = EmployeeForm()

        else:
            context['form'] = EmployeeForm(request.POST)
    else:
        context['form'] = EmployeeForm()
    
    return render(request, 'app/employee.html', context)


def employee_list(request):

    qs_employee = Employee.objects.all().order_by('name', 'pan_number', 'age', 'gender', 'email', 'city')

    paginator = Paginator(qs_employee, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/employee-list.html', {'page_obj': page_obj})

def employee_update(request, pk):
    context = {}
    id = pk
    
    if request.POST:
        obj = get_object_or_404(Employee, id = id)
        form = EmployeeForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Employee updated successfully')
            context['form'] = context['form'] = EmployeeForm()
            return redirect('employee-list')        
        else:
            context['form'] = EmployeeForm(request.POST)
    else:
        data = Employee.objects.get(id=id)
        context['form'] = EmployeeForm(instance=data)
            
        return render(request, "app/employee.html", context)
    return redirect('employee-list')
    
from django.db.models import CharField, ForeignKey, IntegerField
from django.db.models import  Q

def search_employee(request):
    if request.POST:
        criteria = request.POST.get('criteria')
        search = request.POST.get('search')

        if criteria == 'gender':
            qs_employee = Employee.objects.filter(gender__iexact=search)
        elif criteria == 'city':
            qs_employee = Employee.objects.filter(city__city_name__icontains=search)
        else:
            queries = [Q(**{criteria + "__icontains": search})]
            print(queries)

            qs = Q()
            for query in queries:
                qs = qs | query

            qs_employee = Employee.objects.filter(qs)


        paginator = Paginator(qs_employee, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, 'app/employee-list.html', {'page_obj': page_obj})


def delele_employee(request, pk):
    id = pk
    qs_delete = get_object_or_404(Employee, id = id)
    qs_delete.delete()
    return redirect('employee-list')

