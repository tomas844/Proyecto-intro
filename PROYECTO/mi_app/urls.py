from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_app, name='mi_app'),
]
