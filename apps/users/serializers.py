from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from .models import User


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "disabled", "created_at", "updated_at"]


class UserWriteSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField()

    class Meta:
        model = User
        fields= ["email", "password", "password_repeat"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password_repeat": {"write_only": True}
        }

    def validate(self, attrs: dict) -> dict:
        password = attrs.get("password")
        password_repeat = attrs.pop("password_repeat")

        if password != password_repeat:
            raise serializers.ValidationError("Password do not match")

        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return attrs