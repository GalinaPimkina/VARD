from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_creation')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
