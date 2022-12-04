from django.urls import path



from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("searchVehiclePage", views.searchVehiclePage, name = "searchVehiclePage"),
    path("reportvehicle", views.reportVehicle, name = "reportvehicle"),
    path('vehicle/<str:pk>/', views.vehicle, name="vehicle"),
    path('vehicleDetails/', views.vehicleDetails, name="vehicleDetails"),

]