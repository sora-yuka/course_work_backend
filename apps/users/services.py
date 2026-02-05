from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import InvalidToken

User = get_user_model()


class UserService:
    @staticmethod
    def create_user(validated_data: dict):
        return User.objects.create_user(**validated_data)


class TokenService:
    def __init__(self, jwt_response: dict):
        self.data = jwt_response.data
        # Configuration
        self.path = "/"
        self.secure = False
        self.httponly = True
        self.samesite = "Lax"
        self.access_lifetime = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()
        self.refresh_lifetime = settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds()

    def if_token_exists(self, access_token: dict, refresh_token: dict) -> None:
        if not access_token or not refresh_token:
            raise InvalidToken(detail="Token generation failed.")

    def if_access_token_created(self, access_token) -> None:
        if not access_token:
            raise InvalidToken("Access token was not created.")

    def obtain_token(self, response: Response) -> Response:
        access_token = self.data.get("access")
        refresh_token = self.data.get("refresh")

        self.if_token_exists(access_token, refresh_token)

        self._set_cookie(response, "access_token", access_token, self.access_lifetime)
        self._set_cookie(response, "refresh_token", refresh_token, self.refresh_lifetime)
        return response

    def refresh_token(self, response: Response) -> Response:
        access_token = self.data.get("access")

        self.if_access_token_created(access_token)

        self._set_cookie(response, "access_token", access_token, self.access_lifetime)
        return response

    def _set_cookie(self, response: HttpResponse, key, value, max_age) -> None:
        response.set_cookie(
            key=key,
            value=value,
            max_age=int(max_age),
            path=self.path,
            secure=self.secure,
            httponly=self.httponly,
            samesite=self.samesite,
        )