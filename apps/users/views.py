from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserWriteSerializer
from .services import UserService, TokenService


class RegisterUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserWriteSerializer
    service = UserService

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.service.create_user(serializer.validated_data)

        return Response(
            data={"detail": "User created successfully."},
            status=status.HTTP_201_CREATED
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        jwt_response = super().post(request, *args, **kwargs)

        response = Response(
            data={"detail": "Authorization successful."},
            status=status.HTTP_200_OK,
        )

        service = TokenService(jwt_response)
        return service.obtain_token(response)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            if hasattr(request.data, "_mutable"):
                request.data._mutable = True
            request.data["refresh"] = refresh_token

        jwt_token = super().post(request, *args, **kwargs)

        response = Response(
            data={"detail": "Token refresh successful"},
            status=status.HTTP_200_OK
        )

        service = TokenService(jwt_token)
        return service.refresh_token(response)
