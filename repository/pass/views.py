from rest_framework import viewsets, filters

from .models import User, Password
from .serializers import UserSerializer, PasswordSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class PasswordViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Password.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = PasswordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['password', 'description', 'name']
