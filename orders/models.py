from django.db import models
from django.contrib.auth.models import User

import random

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    order_number = models.CharField(max_length=12, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(random.randint(100000, 999999999))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number}"
class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()