from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemStatus(models.TextChoices):
    STOCK = "STOCK", _("In stock")
    SHOWCASE = "SHOWCASE", _("On display")
    REPAIR = "REPAIR", _("To be repaired")
    SOLD = "SOLD", _("Solded")
    LOST = "LOST", _("Item lost")


class MetalType(models.TextChoices):
    GOLD = "GOLD", _("Gold")
    SILVER = "SILVER", _("Silver")
    PLATINUM = "PLATINUM", _("Platinum")
