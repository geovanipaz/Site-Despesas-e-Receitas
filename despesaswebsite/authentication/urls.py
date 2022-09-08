from .views import LoginView, RegistrationView, UsernameValidationView,\
EmailValidationView, LoginView, LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registrar', RegistrationView.as_view(), name='registrar'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout' ),
    path('validar-username', csrf_exempt(UsernameValidationView.as_view())
         , name='validar-username'),
    path('validar-email', csrf_exempt(EmailValidationView.as_view()),
         name='validar-email')
]
