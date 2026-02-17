from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemStatus(models.TextChoices):
    STOCK = "STOCK", _("In stock")
    SHOWCASE = "SHOWCASE", _("On display")
    SOLD = "SOLD", _("Solded")


class MetalType(models.TextChoices):
    GOLD = "GOLD", _("Gold")
    SILVER = "SILVER", _("Silver")
    PLATINUM = "PLATINUM", _("Platinum")


class Currency(models.TextChoices):
    RUB = "RUB", _("RUB")
    USD = "USD", _("USD")
    EUR = "EUR", _("EUR")