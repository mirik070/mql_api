from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class BotApiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(['HELLO WORLD1', 'HELLO WORLD2'])
