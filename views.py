# prediction/views.py
import pickle
import numpy as np
from django.shortcuts import render
from .forms import PredictionForm

# Load the trained model
# Using double backslashes
with open('C:\\Users\\Divya\\OneDrive\\Desktop\\internship\\hdp\\hdp\\heart_disease_model.pkl', 'rb') as file:

    model = pickle.load(file)

def predict_heart_disease(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal'],
            ]])
            prediction = model.predict(data)
            result = 'Positive' if prediction[0] == 1 else 'Negative'
            return render(request, 'prediction/result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'prediction/predict.html', {'form': form})
