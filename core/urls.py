from django.urls import path
from .views import *

urlpatterns = [
    #Vendor Management
    path('api/vendors/', VendorListCreateAPIView.as_view()),#+
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view()),#+

    #Purchase Older
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view()),#+
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view()),#+

    #Performance
    path('api/vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view()),#+

    #Acknowledge
    path('api/purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge_purchase_order'),#+
    
]


