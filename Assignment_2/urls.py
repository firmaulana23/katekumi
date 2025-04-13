from django.contrib import admin
from django.urls import path, include
from .views import StockReportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('report/<str:item_code>/', StockReportView.as_view(), name='stock-report'),
]