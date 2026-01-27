# Data Dictionary - Disease Prediction System

This document describes all features and variables in the dataset.

## Dataset Overview
- **Source**: Patient symptom data
- **Purpose**: Disease prediction and classification
- **Total Features**: TBD based on your specific dataset

## Target Variable

### disease
- **Type**: Categorical
- **Description**: Diagnosis/disease classification for the patient
- **Example values**: "Diabetes", "Hypertension", "Heart Disease", etc.
- **Missing values**: Should be 0 (this is our prediction target)

## Feature Categories

### 1. Demographic Features
Features related to patient demographics.

| Feature Name | Type | Description | Example Values |
|-------------|------|-------------|----------------|
| age | Numerical | Patient age in years | 25, 45, 67 |
| gender | Categorical | Patient gender | Male, Female |
| weight | Numerical | Patient weight (kg) | 65.5, 80.0 |
| height | Numerical | Patient height (cm) | 165, 180 |

### 2. Symptom Features
Binary or categorical features indicating presence/absence of symptoms.

| Feature Name | Type | Description | Possible Values |
|-------------|------|-------------|-----------------|
| fever | Binary | Presence of fever | 0 (No), 1 (Yes) |
| cough | Binary | Presence of cough | 0 (No), 1 (Yes) |
| fatigue | Binary | Presence of fatigue | 0 (No), 1 (Yes) |
| headache | Binary | Presence of headache | 0 (No), 1 (Yes) |

### 3. Clinical Measurements
Quantitative clinical measurements.

| Feature Name | Type | Description | Normal Range |
|-------------|------|-------------|--------------|
| blood_pressure_systolic | Numerical | Systolic BP (mmHg) | 90-120 |
| blood_pressure_diastolic | Numerical | Diastolic BP (mmHg) | 60-80 |
| heart_rate | Numerical | Heart rate (bpm) | 60-100 |
| temperature | Numerical | Body temperature (°C) | 36.5-37.5 |

### 4. Lab Results (if applicable)
Laboratory test results.

| Feature Name | Type | Description | Normal Range |
|-------------|------|-------------|--------------|
| blood_glucose | Numerical | Blood glucose level (mg/dL) | 70-100 |
| cholesterol | Numerical | Cholesterol level (mg/dL) | < 200 |

## Data Quality Notes

### Missing Values
- Document any features with significant missing values
- Describe imputation strategies used

### Outliers
- Identify features prone to outliers
- Document how outliers are handled

### Data Transformations
- List any transformations applied (scaling, encoding, etc.)
- Document feature engineering steps

## Usage Guidelines

1. **Loading Data**: Use pandas to read CSV files
2. **Preprocessing**: Handle missing values before model training
3. **Feature Selection**: Not all features may be relevant for every model
4. **Updates**: Keep this document updated as features change
