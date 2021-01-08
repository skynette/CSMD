from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("register/", views.register, name="register"),
	path("login/", views.login_view, name="login"),
	path("logout/", views.logout_view, name="logout"),

	path("reset_password/", auth_views.PasswordResetView.as_view(
	    template_name="accounts/reset_password.html"), name="reset_password"),
	path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(
	    template_name="accounts/reset_password_sent.html"), name="password_reset_done"),
	path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
	    template_name="accounts/reset.html"), name="password_reset_confirm"),
	path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
	    template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]
