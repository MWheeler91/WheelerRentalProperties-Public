from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.getData),
    path('api/properties/', views.getProperties),
    # path('api/properties/<slug:slug>/', views.getPropertyDetails)
    path('api/properties/get_images/<int:propertyID>/', views.getImages),
    path('api/properties/get_details/<slug:slug>/', views.getPropertyDetails),
    path('api/properties/get_properties/', views.getPropertyDetails),

]