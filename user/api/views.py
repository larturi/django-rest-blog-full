from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User


class RegisterView(APIView):
    def post(self, request):
        return Response(status=status.HTTP_200_OK, data='Todo OK')
