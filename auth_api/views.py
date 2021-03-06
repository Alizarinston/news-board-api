from django.contrib.auth import login, logout
from django.utils.translation import gettext_lazy as _

from rest_framework import status, permissions
from rest_framework.views import APIView, Response

from . import serializers


class LoginView(APIView):
    """ Log in with credentials """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"detail": _("You are already logged in.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.LoginSerializer(
            data=request.data, context={"request": request, "view": self}
        )

        serializer.is_valid(raise_exception=True)
        login(request, serializer.user)
        return Response({"detail": _("Successfully logged in.")})


class LogoutView(APIView):
    @staticmethod
    def get(request):
        logout(request)
        return Response({"detail": _("Successfully logged out.")})


class SignUpView(APIView):
    """ Create a new user instance and log in with the given data """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"detail": _("You are already logged in.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializers.SignUpSerializer(
            data=request.data, context={"request": request, "view": self}
        )

        serializer.is_valid(raise_exception=True)
        login(request, serializer.save())
        return Response({"detail": _("Successfully registered and logged in.")})
