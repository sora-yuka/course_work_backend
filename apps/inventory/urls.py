from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadOnlyItemViewSet, WriteItemViewSet, InventoryAPIView

router = DefaultRouter()
router.register("create", ReadOnlyItemViewSet, "read-only inventory")
router.register("read", WriteItemViewSet, "write inventory")


urlpatterns = [
    path("test/", InventoryAPIView.as_view(), name="get_inventory"),
    path("", include(router.urls)),
]