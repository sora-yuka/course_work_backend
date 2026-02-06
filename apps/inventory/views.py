from rest_framework import status
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


class ReadOnlyItemViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class WriteItemViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class InventoryAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request, *args, **kwargs) -> Response:
        return Response(
            data={"detail": "Inventory test api call"},
            status=status.HTTP_200_OK,
        )