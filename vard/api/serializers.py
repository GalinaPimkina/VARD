from rest_framework import serializers

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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ["user_id", "file_id", "access_type"]


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ["user_id", "name", "link", "publish", "files_type", "type"]

        def get_file_url(self, obj):
            request = self.contex.get("request")
            file_url = obj.fingerprint.url
            return request.build_absolute_url(file_url)


class DashboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"


class ChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chart
        fields = "__all__"


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["user_id", "file_id", "chart_id", "dashboard_id", "comment"]


class ReadCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReadComment
        fields = ["user_id", "comment_id"]


class ConnectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connect
        fields = [
            "user",
            "password",
            "driver",
            "url",
            "host",
            "port",
            "data_base_type",
            "data_base",
            "description",
        ]
