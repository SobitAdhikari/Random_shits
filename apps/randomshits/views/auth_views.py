from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..serializers.authentication_serializers import RegistrationSerializer,LoginSerializer
from ..services.authentication_services import AuthenticationServices,LoginServices

# Create your views here.
#for reg

class RegisterationViews(APIView):

    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = AuthenticationServices.register_user(serializer.validated_data)

        return Response({
                "message": "Now you can access our services with provided credentials",
                "First Name": user.first_name,
                "Last Name": user.last_name,
            }, status=201)

#for login

class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        result = LoginServices.login_user(user)

        return Response({
            "message": "You are welcomed to use our services",
            "user": result["user"],
            "tokens": result["tokens"],
        }, status=status.HTTP_200_OK)
