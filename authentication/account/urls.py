from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("home/", views.home, name="home"),
    path("signout/", views.signout, name="signout"),
    path("passwordchange/<int:pk>/", views.passwordchange, name="passwordchange"),
    path("request-password-reset/", views.request_reset_password, name="request_password_reset"),
    path("reset-password/<int:id>/", views.reset_password, name="reset_password"),
]
