from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Login, name="login"),
    path("", views.Logout, name="logout"),
    path("dashboard", views.Dashboard, name="dashboard"),
    path('journey', views.journey, name="journey"),
    path('vehicle', views.vehicle, name='vehicle'),
    path('fuel', views.fuel, name='fuel'),
    path('tracking', views.tracking, name='tracking'),
    path('vehiclemaintenance', views.vehiclemaintenance, name='vehiclemaintenance'),
    path('vehicleinspection', views.vehicleinspection, name='vehicleinspection'),
    path('vehicleinsuarance', views.vehicleinsuarance, name='vehicleinsuarance'),
    path('vehicleservicing', views.vehicleservicing, name='vehicleservicing'),
    path('fuelingreport', views.fuelingreport, name='fuelingreport'),
    path('jmpreports', views.jmpreports, name='jmpreports'),
    path('trackingreports', views.trackingreports, name='trackingreports'),
    path('drivers', views.drivers, name='drivers'),
    path('approvers', views.approvers, name='approvers'),
    path('vehicles', views.vehicles, name='vehicles'),
    path('viewapprovers', views.view_approvers, name='viewapprovers'),
    path('viewdrivers', views.view_drivers, name='viewdrivers'),
    path('viewjmps', views.view_jmps, name='viewjmps'),
    path('viewfueling', views.view_fueling, name='viewfueling'),
    path('fueling', views.fueling, name='fueling'),
    path('vehicletrackings', views.vehicle_tracking, name='vehicletrackings'),
    path('viewtrackings', views.view_tracking, name='viewtrackings'),
    path('monthlyjmps', views.monthly_jmps, name='monthlyjmps'),
    path('journeymanagement', views.journey_management, name='journeymanagement'),
    path('dailyjmps', views.daily_jmp, name='dailyjmps'),
    path('jmp_daily', views.jmp_daily, name='jmpdaily'),
    path('jmps', views.jmps, name='jmps')
]
