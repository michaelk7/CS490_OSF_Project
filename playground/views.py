from .models import DkaData
from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})
    
def get_data(request):
    field_names = [f.name for f in DkaData._meta.get_fields()]

    return render(request, 'get_data.html', {'field_names': field_names})