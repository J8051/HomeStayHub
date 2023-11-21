from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('<slug:place_slug>', views.accomodation_details),
]