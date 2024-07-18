# prediction/urls.py
from django.urls import path
from prediction.views import predict_heart_disease

urlpatterns = [
    path('', predict_heart_disease, name='predict_heart_disease'),
]
