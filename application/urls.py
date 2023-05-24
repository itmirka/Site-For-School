from django.urls import path
from . import views

urlpatterns = [
	path('', views.application_for_admission)
]
