from django.urls import path

from . import views

app_name = 'accounts'
url_patters = [
    path('signup/', views.signup_view, name="signup")
]
