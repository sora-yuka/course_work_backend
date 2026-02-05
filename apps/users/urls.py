from django.urls import path
from .views import RegisterUserAPIView, CustomTokenObtainPairView, CustomTokenRefreshView, TokenClearView


urlpatterns = [
    path("register/", RegisterUserAPIView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("refresh/", CustomTokenRefreshView.as_view()),
    path("logout/", TokenClearView.as_view()),
]