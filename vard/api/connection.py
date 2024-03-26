from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
import MySQLdb


class ConnectSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    driver = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    host = serializers.CharField(max_length=255)
    port = serializers.IntegerField()
    data_base_type = serializers.CharField(max_length=255)
    data_base = serializers.CharField(max_length=255)
    description = serializers.CharField()


class ConnectionAPI(APIView):
    def post(self, request):
        serializer = ConnectSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)

        try:
            MySQLdb.connect(
                user=request.data['user'],
                password=request.data['password'],
                host=request.data['host'],
                port=request.data['port'],
                database=request.data['data_base'])

            # db.cursor().execute("""CREATE TABLE user2 (
            #                     id INT auto_increment PRIMARY KEY ,
            #                     name CHAR(10) NOT NULL UNIQUE,
            #                     age TINYINT NOT NULL
            #                     );""")
            # db.close()
        except:
            return Response("Required fields: user, password, host, port, data_base. Please, check the field's data is correct.")
        return Response(f"Connection complete")
