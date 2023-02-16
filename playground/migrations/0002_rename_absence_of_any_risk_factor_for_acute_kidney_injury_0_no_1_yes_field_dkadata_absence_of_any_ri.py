# Generated by Django 4.1.5 on 2023-02-10 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dkadata",
            old_name="absence_of_any_risk_factor_for_acute_kidney_injury_0_no_1_yes_field",
            new_name="Absence_Of_Any_Risk_Factor_For_Acute_Kidney_Injury",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="acute_kidney_injury_in_hospital_0_no_1_yes_field",
            new_name="Acute_Kidney_Injury_In_Hospital",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="acute_kidney_injury_on_admission_0_no_1_yes_field",
            new_name="Acute_Kidney_Injury_On_Admission",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="admission_bicarbonate_meq_l_field",
            new_name="Admission_Bicarbonate",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="admission_chloride_meq_l_field",
            new_name="Admission_Chloride",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="admission_glucose_mg_dl_field",
            new_name="Admission_Glucose",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="admission_serum_creatinine_mg_dl_field",
            new_name="Admission_Serum_Creatinine",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="admission_serum_ph",
            new_name="Admission_Serum_pH",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="age_years_field",
            new_name="Age",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="anion_gap_meq_l_field",
            new_name="Anion_Gap",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="apache_ii_score",
            new_name="Apache_II_Score",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="bmi_kg_m2_field",
            new_name="BMI",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="baseline_serum_creatinine_mg_dl_field",
            new_name="Baseline_Serum_Creatinine",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="bicarbonate_nadir_meq_l_field",
            new_name="Bicarbonate_Nadir",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="contrast_media_adminsitered_0_no_1_yes_field",
            new_name="Contrast_Media_Adminsitered",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="delta_gap_meq_l_field",
            new_name="Delta_Gap",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="diabetes_type_type_1_0_type_2_1_field",
            new_name="Diabetes_Type",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="gender_0_male_1_female_field",
            new_name="Gender",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="glucose_nadir_mg_dl_field",
            new_name="Glucose_Nadir",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="glucose_peak_mg_dl_field",
            new_name="Glucose_Peak",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="hospital_length_of_stay_hours_field",
            new_name="Hospital_Length_Of_Stay",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="hypotension_0_no_1_yes_field",
            new_name="Hypotension",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="inappropriate_bicarbonate_use_0_no_1_yes_field",
            new_name="Inappropriate_Bicarbonate_Use",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="infection_as_cause_of_dka_0_no_1_yes_field",
            new_name="Infection_As_Cause_Of_DKA",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="unit_0_medical_icu_1_intermediate_care_field",
            new_name="Medical_Unit",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="nsaid_administration_0_no_1_yes_field",
            new_name="NSAID_Administration",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="new_onset_diabetes_0_no_1_yes_field",
            new_name="New_Onset_Diabetes",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="non_anion_gap_acidosis_0_no_1_yes_field",
            new_name="Non_Anion_Gap_Acidosis",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="noncompliance_to_insulin_at_home_0_no_1_yes_field",
            new_name="Noncompliance_To_Insulin_At_Home",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="other_cause_of_dka_0_no_1_yes_field",
            new_name="Other_Cause_Of_DKA",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="peak_chloride_meq_l_field",
            new_name="Peak_Chloride",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="peak_chloride_category_0_normochloremia_1_hyperchloremia_field",
            new_name="Peak_Chloride_Category",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="peak_serum_creatinine_mg_dl_field",
            new_name="Peak_Serum_Creatinine",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="sepsis_0_no_1_yes_field",
            new_name="Sepsis",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="serum_potassium_maintenane_within_normal_range_0_no_1_yes_field",
            new_name="Serum_Potassium_Maintenane_Within_Normal_Range",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="serum_ph_nadir_field",
            new_name="Serum_pH_Nadir",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="subcutaneous_insulin_overlap_by_1_2_hr_0_no_1_yes_field",
            new_name="Subcutaneous_Insulin_Overlap_By_1_To_2_Hours",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="time_to_final_dka_resolution_hours_field",
            new_name="Time_To_Final_DKA_Resolution",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="time_to_initial_dka_resolution_hours_field",
            new_name="Time_To_Initial_DKA_Resolution",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="total_iv_fluid_volume_ml_field",
            new_name="Total_IV_Fluid_Volume",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="vancomycin_aministration_0_no_1_yes_field",
            new_name="Vancomycin_Aministration",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="volume_of_plasma_lyte_ml_field",
            new_name="Volume_Of_PlasmaLyte",
        ),
        migrations.RenameField(
            model_name="dkadata",
            old_name="weight_kg_field",
            new_name="Weight",
        ),
    ]
