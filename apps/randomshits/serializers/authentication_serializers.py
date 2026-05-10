import re
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError(
                "Password must include at least one special character."
            )

        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value

    def validate(self, attrs):

        phone = attrs.get("phone_number")
        email = attrs.get("email")

        if not phone:
            raise serializers.ValidationError({"phone_number": "Phone number is required."})

        if not email:
            raise serializers.ValidationError({"email": "Email is required."})

        return attrs


from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs): #attrs == validated request data

        identifier = attrs.get("identifier")#receive what client sends
        password = attrs.get("password")

        user = authenticate(#verify 
            username=identifier,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password"
            )

        attrs["user"] = user #sends validate user data with verification in ["user"] i.e. dict format
        return attrs



