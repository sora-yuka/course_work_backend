from typing import Optional
from rest_framework.request import Request
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Optional[tuple]:
        raw_token = request.COOKIES.get("access_token")

        if raw_token:
            validated_token = self.get_validated_token(raw_token)
            try:
                return self.get_user(validated_token), validated_token
            except AuthenticationFailed as e:
                print("Error occured during login: ", e)
        return None