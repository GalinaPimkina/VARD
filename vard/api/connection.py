from rest_framework.response import Response
from rest_framework.views import APIView
import MySQLdb


class ConnectionAPI(APIView):
    def post(self, request):
        try:
            user = request.data['user']
            password = request.data['password']
            driver = request.data['driver']
            url = request.data['url']
            host = request.data['host']
            port = request.data['port']
            data_base_type = request.data['data_base_type']
            data_base = request.data['data_base']
            description = request.data['description']
        except:
            return Response("All fields are required")

        try:
            MySQLdb.connect(user=user, password=password, host=host, port=port, database=data_base)
            # db.cursor().execute("""CREATE TABLE user2 (
            #                     id INT auto_increment PRIMARY KEY ,
            #                     name CHAR(10) NOT NULL UNIQUE,
            #                     age TINYINT NOT NULL
            #                     );""")
            # db.close()
        except:
            return Response("Required fields: driver, user, password, host, port, data_base. Please, check the field's data is correct.")
        return Response(f"Connection complete")
