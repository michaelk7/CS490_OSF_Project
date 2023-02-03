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
    age_years_field = models.IntegerField(db_column='Age (years)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    weight_kg_field = models.FloatField(db_column='Weight (kg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bmi_kg_m2_field = models.FloatField(db_column='BMI (kg/m2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    diabetes_type_type_1_0_type_2_1_field = models.IntegerField(db_column='Diabetes Type (type 1 = 0, type 2 = 1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gender_0_male_1_female_field = models.IntegerField(db_column='Gender (0 = male, 1 = female)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unit_0_medical_icu_1_intermediate_care_field = models.IntegerField(db_column='Unit (0 = Medical ICU, 1 = Intermediate Care)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    apache_ii_score = models.IntegerField(db_column='APACHE II Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admission_chloride_meq_l_field = models.IntegerField(db_column='Admission Chloride (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    peak_chloride_meq_l_field = models.IntegerField(db_column='Peak Chloride (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    peak_chloride_category_0_normochloremia_1_hyperchloremia_field = models.IntegerField(db_column='Peak Chloride Category (0 = normochloremia, 1 = hyperchloremia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    admission_bicarbonate_meq_l_field = models.IntegerField(db_column='Admission Bicarbonate (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bicarbonate_nadir_meq_l_field = models.IntegerField(db_column='Bicarbonate nadir (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseline_serum_creatinine_mg_dl_field = models.FloatField(db_column='Baseline Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    admission_serum_creatinine_mg_dl_field = models.FloatField(db_column='Admission Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    peak_serum_creatinine_mg_dl_field = models.FloatField(db_column='Peak Serum Creatinine (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    admission_serum_ph = models.FloatField(db_column='Admission Serum pH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serum_ph_nadir_field = models.FloatField(db_column='Serum pH Nadir ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    admission_glucose_mg_dl_field = models.IntegerField(db_column='Admission Glucose (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    glucose_peak_mg_dl_field = models.IntegerField(db_column='Glucose Peak (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    glucose_nadir_mg_dl_field = models.IntegerField(db_column='Glucose Nadir (mg/dL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    anion_gap_meq_l_field = models.IntegerField(db_column='Anion Gap (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    delta_gap_meq_l_field = models.IntegerField(db_column='Delta Gap (mEq/L)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    non_anion_gap_acidosis_0_no_1_yes_field = models.IntegerField(db_column='Non-anion Gap Acidosis (0 = no, 1 = yes) ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    volume_of_plasma_lyte_ml_field = models.IntegerField(db_column='Volume of Plasma-Lyte (mL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_iv_fluid_volume_ml_field = models.FloatField(db_column='Total IV Fluid Volume (mL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    time_to_final_dka_resolution_hours_field = models.FloatField(db_column='Time to Final DKA Resolution (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    time_to_initial_dka_resolution_hours_field = models.FloatField(db_column='Time to Initial DKA Resolution (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hospital_length_of_stay_hours_field = models.FloatField(db_column='Hospital Length of Stay (hours)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acute_kidney_injury_on_admission_0_no_1_yes_field = models.IntegerField(db_column='Acute Kidney Injury on Admission (0 = no, 1 yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acute_kidney_injury_in_hospital_0_no_1_yes_field = models.IntegerField(db_column='Acute Kidney Injury In Hospital (0 = no, 1 yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    noncompliance_to_insulin_at_home_0_no_1_yes_field = models.IntegerField(db_column='Noncompliance to Insulin at Home (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    infection_as_cause_of_dka_0_no_1_yes_field = models.IntegerField(db_column='Infection as Cause of DKA (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    new_onset_diabetes_0_no_1_yes_field = models.IntegerField(db_column='New Onset Diabetes (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    other_cause_of_dka_0_no_1_yes_field = models.IntegerField(db_column='Other Cause of DKA (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sepsis_0_no_1_yes_field = models.IntegerField(db_column='Sepsis (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hypotension_0_no_1_yes_field = models.IntegerField(db_column='Hypotension (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contrast_media_adminsitered_0_no_1_yes_field = models.IntegerField(db_column='Contrast Media Adminsitered (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nsaid_administration_0_no_1_yes_field = models.IntegerField(db_column='NSAID Administration (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vancomycin_aministration_0_no_1_yes_field = models.IntegerField(db_column='Vancomycin Aministration (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    absence_of_any_risk_factor_for_acute_kidney_injury_0_no_1_yes_field = models.IntegerField(db_column='Absence of Any Risk Factor for Acute Kidney Injury (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inappropriate_bicarbonate_use_0_no_1_yes_field = models.IntegerField(db_column='Inappropriate Bicarbonate Use (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serum_potassium_maintenane_within_normal_range_0_no_1_yes_field = models.IntegerField(db_column='Serum Potassium Maintenane Within Normal Range (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subcutaneous_insulin_overlap_by_1_2_hr_0_no_1_yes_field = models.FloatField(db_column='Subcutaneous Insulin Overlap by 1-2 hr (0 = no, 1 = yes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        db_table = 'DKA_Data'
