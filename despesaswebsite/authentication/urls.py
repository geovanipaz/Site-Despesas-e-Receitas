from .views import RegistrationView, UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registrar', RegistrationView.as_view(), name='registrar'),
    path('validar-username', csrf_exempt(UsernameValidationView.as_view())
         , name='validar-username')
]
