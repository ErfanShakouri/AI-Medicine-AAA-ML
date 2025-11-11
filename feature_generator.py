import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# تنظیم seed برای تکرارپذیری
np.random.seed(42)
random.seed(42)

# تعداد بیماران
n_patients = 100
n_aaa_positive = 50
n_aaa_negative = 50

# تعریف ستون‌ها
columns = [
    'ID', 'Abdominal Aortic Aneurysm', 'Age (years)', 'Gender', 'Height (cm)', 'Weight (kg)', 'BMI (kg/m²)', 
    'Family History', 'Race', 'CKD', 'CKD Level (1-3)', 'HLP', 'HLP Type', 'HLP Level (1-3)', 'Drinking', 
    'Drinking Level (1-3)', 'Smoker', 'Smoker Level (1-3)', 'Pack_years', 'DM', 'DM Type', 'DM Level (1-3)', 
    'HTN', 'HTN Level (1-3)', 'AS', 'AS Type', 'AS Level (1-3)', 'PAD', 'PAD Level (1-3)', 'CTD', 'CTD Type', 
    'CTD Level (1-3)', 'CVD', 'CVD Type', 'CVD Level (1-3)', 'CD', 'CD Type', 'CD Level (1-3)', 'HDL (mg/dL)', 
    'IHD', 'IHD Level (1-3)', 'COPD', 'COPD Level (1-3)', 'BP', 'SBP (mmHg)', 'DBP (mmHg)', 'HR (bpm)', 
    'O2Sat (%)', 'Abdominal Pain', 'Abdominal Pain Level (1-3)', 'Limb Pain', 'Limb Pain Level (1-3)', 
    'Limb Pain Type', 'Limb Ischemic', 'Limb Ischemic Level (1-3)', 'Mass Effect', 'Aorta calcification', 
    'Aorta Size (mm)', 'MIT (mm)', 'Right CIA (mm)', 'Right EIA (mm)', 'Right IIA (mm)', 'Left CIA (mm)', 
    'Left EIA (mm)', 'Left IIA (mm)', 'Right common carotid', 'Right internal carotid', 'Right external carotid', 
    'Left common carotid', 'Left internal carotid', 'Left external carotid', 'Hemoglobin (g/dL)', 'WBC (cells/µL)', 
    'BUN (mg/dL)', 'Creatinine (mg/dL)', 'Sodium (mmol/L)', 'Potassium (mmol/L)', 'ESR (mm/hr)', 'CRP (mg/L)', 
    'Platelets (1/µL)', 'RBC (cells/µL)', 'Lymphocytes (1/µL)', 'Monocytes (1/µL)', 'Neutrophils (1/µL)', 'RDW (%)', 
    'Abdominal operation', 'Operation Date'
]

# مقادیر ممکن برای کتگوریکال‌ها
gender_options = ['Male', 'Female', 'Others']
family_history_options = ['no', 'Second-degree relatives', 'First-degree relatives']
race_options = ['White', 'Brown', 'Black']
hlp_type_options = ['no', 'Hypercholesterolemia', 'High Triglycerides', 'Mixed']
dm_type_options = ['no', 'Type 1', 'Type 2']
as_type_options = ['no', 'Coronary', 'Peripheral', 'Multi-bed']
ctd_type_options = ['no', 'Marfan', 'Ehlers-Danlos', 'Loeys-Dietz']
cvd_type_options = ['no', 'Ischemic', 'Hemorrhagic', 'TIA']
cd_type_options = ['no', 'Heart Failure', 'Arrhythmia', 'Valvular']
drinking_options = ['No', 'In the past', 'Low', 'Medium', 'High']
smoker_options = ['no', 'Passive', 'In the past', 'yes']
limb_pain_type_options = ['no', 'Claudication', 'Neuropathic', 'Rest Pain']
abdominal_op_options = ['No', 'EVAR', 'Open Surgery']
binary_options = ['no', 'yes']

# تولید داده
data = []
for i in range(n_patients):
    patient = {}
    patient['ID'] = f'P{i+1:03d}'
    patient['Abdominal Aortic Aneurysm'] = 1 if i < n_aaa_positive else 0
    is_aaa = patient['Abdominal Aortic Aneurysm']

    # دموگرافیک
    patient['Age (years)'] = np.random.normal(65, 10) if is_aaa else np.random.normal(55, 10)
    patient['Gender'] = random.choice(gender_options)
    patient['Height (cm)'] = np.random.normal(170, 10)
    patient['Weight (kg)'] = np.random.normal(75, 15)
    patient['BMI (kg/m²)'] = patient['Weight (kg)'] / (patient['Height (cm)'] / 100) ** 2
    patient['Family History'] = random.choices(family_history_options, weights=[0.5, 0.3, 0.2] if is_aaa else [0.7, 0.2, 0.1])[0]
    patient['Race'] = random.choice(race_options)

    # بیماری‌ها و ریسک فاکتورها
    patient['CKD'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['CKD Level (1-3)'] = random.randint(1, 3) if patient['CKD'] == 'yes' else 0
    patient['HLP'] = random.choices(binary_options, weights=[0.6, 0.4] if is_aaa else [0.8, 0.2])[0]
    patient['HLP Type'] = random.choice(hlp_type_options[1:]) if patient['HLP'] == 'yes' else 'no'
    patient['HLP Level (1-3)'] = random.randint(1, 3) if patient['HLP'] == 'yes' else 0
    patient['Drinking'] = random.choice(drinking_options)
    patient['Drinking Level (1-3)'] = random.randint(1, 3) if patient['Drinking'] in ['Low', 'Medium', 'High'] else 0
    patient['Smoker'] = random.choices(smoker_options, weights=[0.3, 0.2, 0.3, 0.2] if is_aaa else [0.5, 0.2, 0.2, 0.1])[0]
    patient['Smoker Level (1-3)'] = random.randint(1, 3) if patient['Smoker'] == 'yes' else 0
    patient['Pack_years'] = np.random.uniform(0, 50) if patient['Smoker'] in ['yes', 'In the past'] else 0
    patient['DM'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['DM Type'] = random.choice(dm_type_options[1:]) if patient['DM'] == 'yes' else 'no'
    patient['DM Level (1-3)'] = random.randint(1, 3) if patient['DM'] == 'yes' else 0
    patient['HTN'] = random.choices(binary_options, weights=[0.5, 0.5] if is_aaa else [0.8, 0.2])[0]
    patient['HTN Level (1-3)'] = random.randint(1, 3) if patient['HTN'] == 'yes' else 0
    patient['AS'] = random.choices(binary_options, weights=[0.6, 0.4] if is_aaa else [0.9, 0.1])[0]
    patient['AS Type'] = random.choice(as_type_options[1:]) if patient['AS'] == 'yes' else 'no'
    patient['AS Level (1-3)'] = random.randint(1, 3) if patient['AS'] == 'yes' else 0
    patient['PAD'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['PAD Level (1-3)'] = random.randint(1, 3) if patient['PAD'] == 'yes' else 0
    patient['CTD'] = random.choices(binary_options, weights=[0.8, 0.2] if is_aaa else [0.95, 0.05])[0]
    patient['CTD Type'] = random.choice(ctd_type_options[1:]) if patient['CTD'] == 'yes' else 'no'
    patient['CTD Level (1-3)'] = random.randint(1, 3) if patient['CTD'] == 'yes' else 0
    patient['CVD'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['CVD Type'] = random.choice(cvd_type_options[1:]) if patient['CVD'] == 'yes' else 'no'
    patient['CVD Level (1-3)'] = random.randint(1, 3) if patient['CVD'] == 'yes' else 0
    patient['CD'] = random.choices(binary_options, weights=[0.6, 0.4] if is_aaa else [0.8, 0.2])[0]
    patient['CD Type'] = random.choice(cd_type_options[1:]) if patient['CD'] == 'yes' else 'no'
    patient['CD Level (1-3)'] = random.randint(1, 3) if patient['CD'] == 'yes' else 0
    patient['IHD'] = random.choices(binary_options, weights=[0.6, 0.4] if is_aaa else [0.9, 0.1])[0]
    patient['IHD Level (1-3)'] = random.randint(1, 3) if patient['IHD'] == 'yes' else 0
    patient['COPD'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['COPD Level (1-3)'] = random.randint(1, 3) if patient['COPD'] == 'yes' else 0

    # آزمایشگاهی
    patient['HDL (mg/dL)'] = np.random.normal(50, 10) if is_aaa else np.random.normal(55, 10)
    patient['Hemoglobin (g/dL)'] = np.random.normal(13, 2)
    patient['WBC (cells/µL)'] = np.random.normal(7000, 2000)
    patient['BUN (mg/dL)'] = np.random.normal(15, 5)
    patient['Creatinine (mg/dL)'] = np.random.normal(1.5, 0.5) if patient['CKD'] == 'yes' else np.random.normal(1, 0.3)
    patient['Sodium (mmol/L)'] = np.random.normal(140, 3)
    patient['Potassium (mmol/L)'] = np.random.normal(4.5, 0.5)
    patient['ESR (mm/hr)'] = np.random.normal(15, 10) if is_aaa else np.random.normal(10, 5)
    patient['CRP (mg/L)'] = np.random.normal(3, 2) if is_aaa else np.random.normal(2, 1)
    patient['Platelets (1/µL)'] = np.random.normal(250000, 50000)
    patient['RBC (cells/µL)'] = np.random.normal(4500000, 500000)
    patient['Lymphocytes (1/µL)'] = np.random.normal(2000, 500)
    patient['Monocytes (1/µL)'] = np.random.normal(500, 100)
    patient['Neutrophils (1/µL)'] = np.random.normal(4000, 1000)
    patient['RDW (%)'] = np.random.normal(13, 1)

    # علائم و نشانه‌ها
    patient['BP'] = random.choices(binary_options, weights=[0.3, 0.7] if is_aaa else [0.5, 0.5])[0]
    patient['SBP (mmHg)'] = np.random.normal(140, 20) if patient['BP'] == 'yes' else 0
    patient['DBP (mmHg)'] = np.random.normal(80, 10) if patient['BP'] == 'yes' else 0
    patient['HR (bpm)'] = np.random.normal(70, 10)
    patient['O2Sat (%)'] = np.random.normal(97, 2)
    patient['Abdominal Pain'] = random.choices(binary_options, weights=[0.6, 0.4] if is_aaa else [0.9, 0.1])[0]
    patient['Abdominal Pain Level (1-3)'] = random.randint(1, 3) if patient['Abdominal Pain'] == 'yes' else 0
    patient['Limb Pain'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.9, 0.1])[0]
    patient['Limb Pain Type'] = random.choice(limb_pain_type_options[1:]) if patient['Limb Pain'] == 'yes' else 'no'
    patient['Limb Pain Level (1-3)'] = random.randint(1, 3) if patient['Limb Pain'] == 'yes' else 0
    patient['Limb Ischemic'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.95, 0.05])[0]
    patient['Limb Ischemic Level (1-3)'] = random.randint(1, 3) if patient['Limb Ischemic'] == 'yes' else 0
    patient['Mass Effect'] = random.choices(binary_options, weights=[0.7, 0.3] if is_aaa else [0.95, 0.05])[0]

    # اولتراسوند
    patient['Aorta Size (mm)'] = np.random.normal(40, 10) if is_aaa else np.random.normal(20, 5)
    patient['Aorta calcification'] = random.choices(binary_options, weights=[0.5, 0.5] if is_aaa else [0.9, 0.1])[0]
    patient['MIT (mm)'] = np.random.normal(5, 2) if is_aaa else 0
    patient['Right CIA (mm)'] = np.random.normal(15, 5) if is_aaa else np.random.normal(10, 3)
    patient['Right EIA (mm)'] = np.random.normal(10, 3)
    patient['Right IIA (mm)'] = np.random.normal(8, 2)
    patient['Left CIA (mm)'] = np.random.normal(15, 5) if is_aaa else np.random.normal(10, 3)
    patient['Left EIA (mm)'] = np.random.normal(10, 3)
    patient['Left IIA (mm)'] = np.random.normal(8, 2)
    patient['Right common carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]
    patient['Right internal carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]
    patient['Right external carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]
    patient['Left common carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]
    patient['Left internal carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]
    patient['Left external carotid'] = random.choices(binary_options, weights=[0.8, 0.2])[0]

    # جراحی
    patient['Abdominal operation'] = random.choices(abdominal_op_options, weights=[0.4, 0.3, 0.3] if is_aaa else [0.95, 0.025, 0.025])[0]
    if patient['Abdominal operation'] != 'No':
        start_date = datetime(2020, 1, 1)
        days_range = (datetime(2025, 10, 25) - start_date).days
        random_days = random.randint(0, days_range)
        patient['Operation Date'] = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    else:
        patient['Operation Date'] = ''

    data.append(patient)

# ایجاد DataFrame
df = pd.DataFrame(data, columns=columns)

# گرد کردن مقادیر عددی
numeric_cols = ['Age (years)', 'Height (cm)', 'Weight (kg)', 'BMI (kg/m²)', 'Pack_years', 'HDL (mg/dL)', 
                'SBP (mmHg)', 'DBP (mmHg)', 'HR (bpm)', 'O2Sat (%)', 'Aorta Size (mm)', 'MIT (mm)', 
                'Right CIA (mm)', 'Right EIA (mm)', 'Right IIA (mm)', 'Left CIA (mm)', 'Left EIA (mm)', 
                'Left IIA (mm)', 'Hemoglobin (g/dL)', 'WBC (cells/µL)', 'BUN (mg/dL)', 'Creatinine (mg/dL)', 
                'Sodium (mmol/L)', 'Potassium (mmol/L)', 'ESR (mm/hr)', 'CRP (mg/L)', 'Platelets (1/µL)', 
                'RBC (cells/µL)', 'Lymphocytes (1/µL)', 'Monocytes (1/µL)', 'Neutrophils (1/µL)', 'RDW (%)']
for col in numeric_cols:
    df[col] = df[col].round(1)

# ذخیره به CSV
df.to_csv('synthetic_aaa_100.csv', index=False)

# ذخیره به اکسل (در صورت نیاز)
#df.to_excel('synthetic_aaa_100.xlsx', index=False)

# بررسی خلاصه
print("شکل دیتاست:", df.shape)
print("توزیع AAA:\n", df['Abdominal Aortic Aneurysm'].value_counts())
print("ستون‌ها:", df.columns.tolist())
print("نمونه داده‌ها:\n", df.head())