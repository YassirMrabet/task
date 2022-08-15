from django.urls import path

from . import views

urlpatterns = [
    path('reservations', views.rentals_with_previous, name='reservations'),
]