from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class UserCreateAPIView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     authentication_classes = []
     permission_classes = []

class LogoutAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token associated with the current user
        Token.objects.filter(user=request.user).delete()
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
