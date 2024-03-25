from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import create_engine


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
            return Response("Не заполнены необходимые поля для подключения")

        engine = create_engine(f"{data_base_type}+{driver}://{user}:{password}@{host}:{port}/{data_base}", echo=True)
        try:
            engine.connect()
        except:
            return Response("Invalid data")
        return Response("Connection complete")

