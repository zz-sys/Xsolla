from django.db import models


class Product(models.Model):
    type = models.CharField(unique=True, max_length=800, blank=False)


class StockUnit(models.Model):
    sku = models.PositiveIntegerField(unique=True, blank=False, primary_key=True)
    description = models.TextField(blank=False)
    product_type = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)


class UnitAtStorage(models.Model):
    sku = models.OneToOneField(StockUnit, on_delete=models.DO_NOTHING, blank=False, unique=True)
    cost = models.PositiveIntegerField(blank=False)
    count = models.PositiveSmallIntegerField(blank=False)
