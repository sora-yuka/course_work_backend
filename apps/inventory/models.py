from django.db import models
from internal import choices


class Item(models.Model):
    title = models.CharField(max_length=250)
    unique_identification_number = models.CharField(max_length=16, unique=True) # УИН ГИИС
    stock_keeping_unit = models.CharField(max_length=50, unique=True) # Артикунл
    description = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=4, decimal_places=1)
    status = models.CharField(
        max_length=20,
        choices=choices.ItemStatus.choices,
        default=choices.ItemStatus.STOCK
    )
    metal = models.CharField(max_length=20, choices=choices.MetalType)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_display = models.ImageField(upload_to="items")

    def __str__(self) -> str: return f"{self.unique_identification_number}, {self.stock_keeping_unit}, {self.title}"
