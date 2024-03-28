import MySQLdb
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import (
    UserSerializer,
    AccessSerializer,
    FileSerializer,
    DashboardSerializer,
    ChartSerializer,
    FeedbackSerializer,
    CommentSerializer,
    ReadCommentSerializer,
    ConnectSerializer,
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
    Connect,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_creation")
    serializer_class = UserSerializer


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


class FileAPI(APIView):
    # TO DO
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()

    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class ConnectViewSet(viewsets.ModelViewSet):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer


class ConnectAPI(APIView):
    def post(self, request):
        serializer = ConnectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()

        try:
            MySQLdb.connect(
                user=request.data["user"],
                password=request.data["password"],
                host=request.data["host"],
                port=request.data["port"],
                database=request.data["data_base"],
            )

            # db.cursor().execute("""CREATE TABLE user2 (
            #                     id INT auto_increment PRIMARY KEY ,
            #                     name CHAR(10) NOT NULL UNIQUE,
            #                     age TINYINT NOT NULL
            #                     );""")
            # db.close()
        except:
            return Response("Please, check the fields data is correct.")
        return Response(f"Connection complete")
