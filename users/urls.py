from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from config import settings
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, ActivateView, VerificationFailedView, VerificationSuccessView
from users.views import UserPasswordResetConfirmView, RegistrationEmailSentView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_need_verify', RegistrationEmailSentView.as_view(), name='register_need_verify'),
    path('verification_failed/', VerificationFailedView.as_view(), name='verification_failed'),
    path('verification_success/', VerificationSuccessView.as_view(), name='verification_success'),
    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        html_email_template_name='users/password_reset_email.html',
        email_template_name='users/password_reset_email.html',
        from_email=settings.EMAIL_HOST_USER,
        success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(
        success_url=reverse_lazy('users:password_reset_complete'),
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
