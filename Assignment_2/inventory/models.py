from django.db import models

class Item(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Purchase(models.Model):
    code = models.CharField(max_length=10, unique=True)
    date = models.DateField()
    description = models.TextField()

class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='details', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=10)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class Sell(models.Model):
    code = models.CharField(max_length=10, unique=True)
    date = models.DateField()
    description = models.TextField()

class SellDetail(models.Model):
    sell = models.ForeignKey(Sell, related_name='details', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=10)
    quantity = models.IntegerField()