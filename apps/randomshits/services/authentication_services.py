from ..models import   User,Notification
from rest_framework_simplejwt.tokens import RefreshToken

class AuthenticationServices:

    @staticmethod
    def register_user(validated_data):

        # Create user (handles password hashing)
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
        )
        return user
    
from rest_framework_simplejwt.tokens import RefreshToken

class LoginServices:

    @staticmethod
    def get_refresh_token(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access_token": str(refresh.access_token),
        }

    @staticmethod
    def login_user(user):

        tokens = LoginServices.get_refresh_token(user)
        Notification.objects.create(
            user=user,
            title="New Login",
            message="You logged in successfully"
        )

        return {
            "user": {
                "id": user.id,
                "First Name":user.first_name,
                "Last Name":user.last_name,
                "email": user.email,
                "phone_number": str(user.phone_number),
            },
            "tokens": tokens,
        }