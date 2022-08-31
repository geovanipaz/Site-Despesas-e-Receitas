from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path('registrar', RegistrationView.as_view(), name='registrar')
]
