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


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReadCommentViewSet(viewsets.ModelViewSet):
    queryset = ReadComment.objects.all()
    serializer_class = ReadCommentSerializer
