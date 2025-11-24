# accounts/views.py
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from rest_framework import status

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    permission_classes = [AllowAny]

    def get_response(self):
        """
        Override to set HttpOnly cookies for access and refresh tokens.
        dj-rest-auth's SocialLoginView will call `login()` and create a user.
        We'll generate RefreshToken.for_user and set cookies, then return a small JSON response.
        """
        user = self.user  # set by SocialLoginView on successful social login
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        resp = Response({"detail": "Login successful"}, status=status.HTTP_200_OK)

        # Set cookies (HttpOnly)
        # For dev use secure=False; set secure=True in production with HTTPS
        resp.set_cookie(
            key="access",
            value=access_token,
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()),
        )
        resp.set_cookie(
            key="refresh",
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=int(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds()),
        )
        return resp

# Endpoint para retornar dados do usuário autenticado
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        u = request.user
        return Response({
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "first_name": u.first_name,
            "last_name": u.last_name,
        })

# Logout: limpa cookies e, opcionalmente, invalida refresh (precisa tratar blacklist)
from rest_framework.views import APIView

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resp = Response({"detail": "Logged out"}, status=status.HTTP_200_OK)
        resp.delete_cookie("access")
        resp.delete_cookie("refresh")
        return resp
