from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import (
    UserSerializer,
    AccessSerializer,
    FileSerializer,
    DashboardSerializer,
    ChartSerializer,
    FeedbackSerializer,
    CommentSerializer,
    ReadCommentSerializer,
)
from users.models import (
    User,
    Access,
    File,
    Dashboard,
    Chart,
    Feedback,
    Comment,
    ReadComment,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_creation")
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


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReadCommentViewSet(viewsets.ModelViewSet):
    queryset = ReadComment.objects.all()
    serializer_class = ReadCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
