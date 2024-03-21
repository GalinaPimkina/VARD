from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import UserSerializer, AccessSerializer, FileSerializer
from users.models import User, Access, File


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_creation')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]
