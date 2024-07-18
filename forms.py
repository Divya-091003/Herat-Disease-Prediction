# prediction/forms.py
from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.IntegerField(label='Sex (0 = female, 1 = male)')
    cp = forms.IntegerField(label='Chest Pain Type')
    trestbps = forms.IntegerField(label='Resting Blood Pressure')
    chol = forms.IntegerField(label='Serum Cholesterol (mg/dl)')
    fbs = forms.IntegerField(label='Fasting Blood Sugar > 120 mg/dl (0 = no, 1 = yes)')
    restecg = forms.IntegerField(label='Resting Electrocardiographic Results')
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved')
    exang = forms.IntegerField(label='Exercise Induced Angina (0 = no, 1 = yes)')
    oldpeak = forms.FloatField(label='ST Depression Induced by Exercise Relative to Rest')
    slope = forms.IntegerField(label='Slope of the Peak Exercise ST Segment')
    ca = forms.IntegerField(label='Number of Major Vessels (0-3) Colored by Flourosopy')
    thal = forms.IntegerField(label='Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)')
#C:\Users\Divya\OneDrive\Desktop\internship\hdp\prediction\froms.py