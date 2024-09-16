from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, ProfileSerializer
from .permissions import IsUserOrReadOnly


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfilesView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = User.objects.all()


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
