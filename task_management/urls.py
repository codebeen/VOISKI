from django.urls import path

from .views import *

urlpatterns = [
    path("", display_login_form, name="show_login"),
    path("create-account", display_create_acount_form, name="show_create_account"),
    path("forgot-password", display_forgot_password_form, name="show_forgot_password"),
]