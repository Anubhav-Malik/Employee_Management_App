from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return redirect('/emp')
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp')
            except:
                pass
    else:
        form = EmployeeForm()

    employees = Employee.objects.all()
    return render(request,'index.html',{'form':form,'employees':employees})
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/emp")
    return render(request, 'edit.html', {'employee': employee})

