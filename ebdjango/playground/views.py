from .forms import DkaForm
from .forms import SavedForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import DkaData

from joblib import load
model = load('./../savedModels/models.joblib')

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})
    
def get_data(request):
    if request.method == "POST":
        form = SavedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(results)
    else:
        form = DkaForm()
    context= {'form': form }
    return render(request, 'get_data.html', context)

def input(request):
    template = loader.get_template('input.html')
    return HttpResponse(template.render())

def results(request):
    patients = DkaData.objects.all().values()
    template = loader.get_template('results.html')
    context = {
    'patients': patients,
    }
    return HttpResponse(template.render(context, request))

def predictions(request):
    if request.method == "POST":
        y_pred = model.predict(DkaData.objects.all().values())
        print(y_pred)
        return render(request, 'results.html')