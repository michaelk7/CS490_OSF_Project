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
        obj = DkaData()
        queryset = []
        if form.is_valid():

            #create object with all fields

            obj.Age = form.cleaned_data['Age']
            obj.Weight = form.cleaned_data['Weight']
            obj.BMI = form.cleaned_data['BMI']
            obj.Diabetes_Type = form.cleaned_data['Diabetes_Type']
            obj.Gender = form.cleaned_data['Gender']
            obj.Medical_Unit = form.cleaned_data['Medical_Unit']
            obj.Apache_II_Score = form.cleaned_data['Apache_II_Score']
            obj.Admission_Chloride = form.cleaned_data['Admission_Chloride']
            obj.Peak_Chloride = form.cleaned_data['Peak_Chloride']
            obj.Peak_Chloride_Category = form.cleaned_data['Peak_Chloride_Category']
            obj.Admission_Bicarbonate = form.cleaned_data['Admission_Bicarbonate']
            obj.Bicarbonate_Nadir = form.cleaned_data['Bicarbonate_Nadir']
            obj.Baseline_Serum_Creatinine = form.cleaned_data['Baseline_Serum_Creatinine']
            obj.Admission_Serum_Creatinine = form.cleaned_data['Admission_Serum_Creatinine']
            obj.Peak_Serum_Creatinine = form.cleaned_data['Peak_Serum_Creatinine']
            obj.Admission_Serum_pH = form.cleaned_data['Admission_Serum_pH']
            obj.Serum_pH_Nadir = form.cleaned_data['Serum_pH_Nadir']
            obj.Admission_Glucose = form.cleaned_data['Admission_Glucose']
            obj.Glucose_Peak = form.cleaned_data['Glucose_Peak']
            obj.Glucose_Nadir = form.cleaned_data['Glucose_Nadir']
            obj.Anion_Gap = form.cleaned_data['Anion_Gap']
            obj.Delta_Gap = form.cleaned_data['Delta_Gap']
            obj.Non_Anion_Gap_Acidosis = form.cleaned_data['Non_Anion_Gap_Acidosis']
            obj.Volume_Of_PlasmaLyte = form.cleaned_data['Volume_Of_PlasmaLyte']
            obj.Total_IV_Fluid_Volume = form.cleaned_data['Total_IV_Fluid_Volume']
            obj.Time_To_Final_DKA_Resolution = form.cleaned_data['Time_To_Final_DKA_Resolution']
            obj.Time_To_Initial_DKA_Resolution = form.cleaned_data['Time_To_Initial_DKA_Resolution']
            obj.Hospital_Length_Of_Stay = form.cleaned_data['Hospital_Length_Of_Stay']
            obj.Acute_Kidney_Injury_On_Admission = form.cleaned_data['Acute_Kidney_Injury_On_Admission']
            obj.Acute_Kidney_Injury_In_Hospital = form.cleaned_data['Acute_Kidney_Injury_In_Hospital']
            obj.Noncompliance_To_Insulin_At_Home = form.cleaned_data['Noncompliance_To_Insulin_At_Home']
            obj.Infection_As_Cause_Of_DKA = form.cleaned_data['Infection_As_Cause_Of_DKA']
            obj.New_Onset_Diabetes = form.cleaned_data['New_Onset_Diabetes']
            obj.Other_Cause_Of_DKA = form.cleaned_data['Other_Cause_Of_DKA']
            obj.Sepsis = form.cleaned_data['Sepsis']
            obj.Hypotension = form.cleaned_data['Hypotension']
            obj.Contrast_Media_Adminsitered = form.cleaned_data['Contrast_Media_Adminsitered']
            obj.NSAID_Administration = form.cleaned_data['NSAID_Administration']
            obj.Vancomycin_Aministration = form.cleaned_data['Vancomycin_Aministration']
            obj.Absence_Of_Any_Risk_Factor_For_Acute_Kidney_Injury = form.cleaned_data['Absence_Of_Any_Risk_Factor_For_Acute_Kidney_Injury']
            obj.Inappropriate_Bicarbonate_Use = form.cleaned_data['Inappropriate_Bicarbonate_Use']
            obj.Serum_Potassium_Maintenane_Within_Normal_Range = form.cleaned_data['Serum_Potassium_Maintenane_Within_Normal_Range']
            obj.Subcutaneous_Insulin_Overlap_By_1_To_2_Hours = form.cleaned_data['Subcutaneous_Insulin_Overlap_By_1_To_2_Hours']
            

            obj.save()


            queryset.append(obj.Age)
            queryset.append(obj.Weight)
            queryset.append(obj.BMI)
            queryset.append(obj.Diabetes_Type)
            queryset.append(obj.Gender)
            queryset.append(obj.Medical_Unit)
            queryset.append(obj.Apache_II_Score)
            queryset.append(obj.Admission_Chloride)
            queryset.append(obj.Peak_Chloride)
            queryset.append(obj.Peak_Chloride_Category)
            queryset.append(obj.Admission_Bicarbonate)
            queryset.append(obj.Bicarbonate_Nadir)
            queryset.append(obj.Baseline_Serum_Creatinine)
            queryset.append(obj.Admission_Serum_Creatinine)
            queryset.append(obj.Peak_Serum_Creatinine)
            queryset.append(obj.Admission_Serum_pH)
            queryset.append(obj.Serum_pH_Nadir)
            queryset.append(obj.Admission_Glucose)
            queryset.append(obj.Glucose_Peak)
            queryset.append(obj.Glucose_Nadir)
            queryset.append(obj.Anion_Gap)
            queryset.append(obj.Delta_Gap)
            queryset.append(obj.Non_Anion_Gap_Acidosis)
            queryset.append(obj.Volume_Of_PlasmaLyte)
            queryset.append(obj.Total_IV_Fluid_Volume)
            queryset.append(obj.Time_To_Final_DKA_Resolution)
            queryset.append(obj.Time_To_Initial_DKA_Resolution)
            queryset.append(obj.Hospital_Length_Of_Stay)
            queryset.append(obj.Acute_Kidney_Injury_On_Admission)
            queryset.append(obj.Acute_Kidney_Injury_In_Hospital)
            queryset.append(obj.Noncompliance_To_Insulin_At_Home)
            queryset.append(obj.Infection_As_Cause_Of_DKA)
            queryset.append(obj.New_Onset_Diabetes)
            queryset.append(obj.Other_Cause_Of_DKA)
            queryset.append(obj.Sepsis)
            queryset.append(obj.Hypotension)
            queryset.append(obj.Contrast_Media_Adminsitered)
            queryset.append(obj.NSAID_Administration)
            queryset.append(obj.Vancomycin_Aministration)
            queryset.append(obj.Absence_Of_Any_Risk_Factor_For_Acute_Kidney_Injury)
            queryset.append(obj.Inappropriate_Bicarbonate_Use)
            queryset.append(obj.Serum_Potassium_Maintenane_Within_Normal_Range)
            queryset.append(obj.Subcutaneous_Insulin_Overlap_By_1_To_2_Hours)

            y_pred = model.predict([queryset])
            context = {'result':y_pred}
            template = loader.get_template('results.html')
            return render(request, 'results.html', context)
    else:
        form = DkaForm()
    context= {'form': form }
    return render(request, 'get_data.html', context)

def input(request):
    template = loader.get_template('input.html')
    return HttpResponse(template.render())

def results(request):
    queryset = form.cleaned_data['age']
        
    y_pred = model.predict([queryset])
    context = {'result':y_pred}
    template = loader.get_template('results.html')
    return render(request, 'results.html', context)