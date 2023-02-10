# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DkaData(models.Model):
    id = models.IntegerField(primary_key=True)
    Age = models.IntegerField(db_column='Age (years)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Weight = models.FloatField(db_column='Weight (kg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    BMI = models.FloatField(db_column='BMI (kg/m2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Diabetes_Type = models.IntegerField(db_column='Diabetes Type (type 1 = 0, type 2 = 1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Gender = models.IntegerField(db_column='Gender (0 = male, 1 = female)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Medical_Unit = models.IntegerField(db_column='Unit (0 = Medical ICU, 1 = Intermediate Care)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Apache_II_Score = models.IntegerField(db_column='APACHE II Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    Admission_Chloride = models.IntegerField(db_column='Admission Chloride (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Peak_Chloride = models.IntegerField(db_column='Peak Chloride (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Peak_Chloride_Category = models.IntegerField(db_column='Peak Chloride Category (0 = normochloremia, 1 = hyperchloremia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Admission_Bicarbonate = models.IntegerField(db_column='Admission Bicarbonate (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Bicarbonate_Nadir = models.IntegerField(db_column='Bicarbonate nadir (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Baseline_Serum_Creatinine = models.FloatField(db_column='Baseline Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Admission_Serum_Creatinine = models.FloatField(db_column='Admission Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Peak_Serum_Creatinine = models.FloatField(db_column='Peak Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Admission_Serum_pH = models.FloatField(db_column='Admission Serum pH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    Serum_pH_Nadir = models.FloatField(db_column='Serum pH Nadir ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Admission_Glucose = models.IntegerField(db_column='Admission Glucose (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Glucose_Peak = models.IntegerField(db_column='Glucose Peak (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Glucose_Nadir = models.IntegerField(db_column='Glucose Nadir (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Anion_Gap = models.IntegerField(db_column='Anion Gap (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Delta_Gap = models.IntegerField(db_column='Delta Gap (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Non_Anion_Gap_Acidosis = models.IntegerField(db_column='Non-anion Gap Acidosis (0 = no, 1 = yes) ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Volume_Of_PlasmaLyte = models.IntegerField(db_column='Volume of Plasma-Lyte (mL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Total_IV_Fluid_Volume = models.FloatField(db_column='Total IV Fluid Volume (mL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Time_To_Final_DKA_Resolution = models.FloatField(db_column='Time to Final DKA Resolution (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Time_To_Initial_DKA_Resolution = models.FloatField(db_column='Time to Initial DKA Resolution (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Hospital_Length_Of_Stay = models.FloatField(db_column='Hospital Length of Stay (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Acute_Kidney_Injury_On_Admission = models.IntegerField(db_column='Acute Kidney Injury on Admission (0 = no, 1 yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Acute_Kidney_Injury_In_Hospital = models.IntegerField(db_column='Acute Kidney Injury In Hospital (0 = no, 1 yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Noncompliance_To_Insulin_At_Home = models.IntegerField(db_column='Noncompliance to Insulin at Home (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Infection_As_Cause_Of_DKA = models.IntegerField(db_column='Infection as Cause of DKA (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    New_Onset_Diabetes = models.IntegerField(db_column='New Onset Diabetes (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Other_Cause_Of_DKA = models.IntegerField(db_column='Other Cause of DKA (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Sepsis = models.IntegerField(db_column='Sepsis (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Hypotension = models.IntegerField(db_column='Hypotension (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Contrast_Media_Adminsitered = models.IntegerField(db_column='Contrast Media Adminsitered (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    NSAID_Administration = models.IntegerField(db_column='NSAID Administration (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Vancomycin_Aministration = models.IntegerField(db_column='Vancomycin Aministration (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Absence_Of_Any_Risk_Factor_For_Acute_Kidney_Injury = models.IntegerField(db_column='Absence of Any Risk Factor for Acute Kidney Injury (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Inappropriate_Bicarbonate_Use = models.IntegerField(db_column='Inappropriate Bicarbonate Use (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Serum_Potassium_Maintenane_Within_Normal_Range = models.IntegerField(db_column='Serum Potassium Maintenane Within Normal Range (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Subcutaneous_Insulin_Overlap_By_1_To_2_Hours = models.FloatField(db_column='Subcutaneous Insulin Overlap by 1-2 hr (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        db_table = 'DKA_Data'
