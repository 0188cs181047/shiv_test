from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from testapp.models import Employee
def index(request):
    return render(request,'testapp/index.html')

def empriew(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'testapp/emoinfo.html' ,{'emp_list':emp_list})

# def data(request):
#     c = 'hii good morning ,good evening, good aftenoon, goos nigh'
#     my_fict= {'c':c}
#     return render(request , 'testapp/emoinfo.html',{'c':c})
