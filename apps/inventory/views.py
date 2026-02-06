from rest_framework import status
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .services import ItemService


class ReadOnlyItemViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = ItemService.get_all_objects()
    serializer_class = ItemService.read_serializer_class


class WriteItemViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = ItemService.get_all_objects()
    serializer_class = ItemService.write_serializer_class


class StockOnlyItemView(ListAPIView):
    queryset = ItemService.get_all_stock()
    serializer_class = ItemService.read_serializer_class


class ShowcaseOnlyItemView(ListAPIView):
    queryset = ItemService.get_all_showcase()
    serializer_class = ItemService.read_serializer_class


class SoldOnlyItemView(ListAPIView):
    queryset = ItemService.get_all_sold()
    serializer_class = ItemService.read_serializer_class
