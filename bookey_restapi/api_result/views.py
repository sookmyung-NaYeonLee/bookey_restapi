from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResultSerializer
from rest_framework import status
from .models import Result

class ResultView(APIView):
    def get(self, request, **kwargs):
        return Response(status=status.HTTP_200_OK)
