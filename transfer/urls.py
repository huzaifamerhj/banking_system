from django.urls import path
from . import views
urlpatterns = [
    
    path('transfer/', views.transfer, name="transfer"),
    path('customer/',views.customer_details, name="customer"),
    path('transfer_details/',views.transfer_details, name="transfer_details"),
    
]