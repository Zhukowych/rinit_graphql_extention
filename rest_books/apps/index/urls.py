from django.urls import path
from .views import *
from rest_framework.authtoken import views

app_name="index"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('example/', TokenAuthorizationTest.as_view(), name="example"),
]
