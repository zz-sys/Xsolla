from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register('api/products', ProductViewSet, basename=Product)
router.register('api/stockunits', StockUnitViewSet, basename=StockUnit)
router.register('api/units', UnitAtStorageViewSet, basename=UnitAtStorage)
urlpatterns = router.urls + [
]