from django.contrib import admin
from django.urls import path,include
from . import views
from .views import VehiclesApi

# from .views import VehiclesApi, VehicleView, excel_page_api

urlpatterns = [
    path('vehicles/', views.VehiclesApi.as_view(), name='VehiclesApi'),
    path('vehicles/<int:pk>/', views.VehiclesApi.as_view(), name='VehiclesApi'),
    # path('ev_excel/', views.excel_page_api, name='excel_page_api'),
    path('ev/vehicles/standard_car/', views.ev_filter_standard_vehicle.as_view(), name='ev_filter_vehicle'),
    path('ev/vehicles/best_car/', views.ev_filter_best_vehicle.as_view(), name='ev_filter_vehicle'),
    path('ev/vehicles/all_best_car/', views.ev_filter_all_best_vehicle.as_view(), name='ev_filter_vehicle'),
    path('ev/vehicles/all_standard_car/', views.ev_filter_all_standard_vehicle.as_view(), name='ev_filter_vehicle'),
    path('ev/vehicles/dropdown/', views.ev_vehicle_dropdown.as_view(), name='ev_filter_dropdown_vehicle'),

    # path('Ev_vehicles/version/', views.ev_vehicle_version_dropdown.as_view(), name='ev_vehicle_version_dropdown'),
    path('vs/vehicles/<int:pk>/', views.vs_car_list.as_view(), name='vs_filter_dropdown_vehicle'),
    path('vs/vehicles/', views.vs_car_list.as_view(), name='vs_filter_dropdown_vehicle'),
    path('vs/vehicles/dropdown/', views.vs_vehicle_dropdown.as_view(), name='vs_filter_dropdown_vehicle'),
     path('ev/vehicles/agreement/', views.ev_car_agreement.as_view(), name='ev_car_agreement'),

]

# http://127.0.0.1:8000/vehicles/?ispublished=true
# http://127.0.0.1:8000/vehicles/?ispublished=false
# http://127.0.0.1:8000/vehicles/



