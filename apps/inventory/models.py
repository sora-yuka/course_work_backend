from django.db import models
from internal.choices import ItemStatus, MetalType


class Item(models.Model):
    unique_identification_number = models.CharField(max_length=16, unique=True) # УИН ГИИС
    stock_keeping_unit = models.CharField(max_length=50) # Артикунл
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=4, decimal_places=1)
    status = models.CharField(
        max_length=20,
        choices=ItemStatus.choices,
        default=ItemStatus.STOCK
    )
    metal = models.CharField(max_length=20, choices=MetalType.choices)
    price_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.unique_identification_number} | {self.stock_keeping_unit}"
