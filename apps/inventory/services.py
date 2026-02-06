from .models import Item
from .serializers import ItemReadSerializer, ItemWriteSerializer
from internal.choices import MetalType, ItemStatus


class ItemService:
    read_serializer_class = ItemReadSerializer
    write_serializer_class = ItemWriteSerializer

    @staticmethod
    def get_all_objects():
        return Item.objects.all()

    @staticmethod
    def get_all_stock():
        return Item.objects.filter(status=ItemStatus.STOCK)

    @staticmethod
    def get_all_showcase():
        return Item.objects.filter(status=ItemStatus.SHOWCASE)

    @staticmethod
    def get_all_sold():
        return Item.objects.filter(status=ItemStatus.SOLD)