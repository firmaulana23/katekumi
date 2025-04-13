from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, PurchaseViewSet, SellViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sells', SellViewSet)

urlpatterns = [
    path('', include(router.urls)),
]