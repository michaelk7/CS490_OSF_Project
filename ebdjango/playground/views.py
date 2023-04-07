from .forms import DkaForm
from .forms import SavedForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import DkaData

from joblib import load
model = load('./../savedModels/models.joblib')

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
    queryset = DkaData.objects.values_list().first()
        
    y_pred = model.predict([queryset])
    context = {'result':y_pred}
    template = loader.get_template('results.html')
    return render(request, 'results.html', context)