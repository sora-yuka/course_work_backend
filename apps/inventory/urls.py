from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("read", views.ReadOnlyItemViewSet, "read-only inventory")
router.register("write", views.WriteItemViewSet, "write inventory")


urlpatterns = [
    path("", include(router.urls)),
]
