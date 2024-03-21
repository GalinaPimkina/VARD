from rest_framework import serializers

from users.models import User, Access, File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ['user_id', 'file_id', 'access_type']


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'link', 'publish', 'files_type', 'type']