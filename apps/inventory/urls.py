from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("read", views.ReadOnlyItemViewSet, "write inventory")
router.register("create", views.WriteItemViewSet, "read-only inventory")


urlpatterns = [
    path("stock/", views.StockOnlyItemView.as_view()),
    path("showcase/", views.ShowcaseOnlyItemView.as_view()),
    path("sold/", views.SoldOnlyItemView.as_view()),
    path("", include(router.urls)),
]