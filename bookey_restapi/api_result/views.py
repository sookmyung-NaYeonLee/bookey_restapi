from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResultSerializer
from rest_framework import status
from .models import Result

class ResultView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('bid') is None:
            result_queryset = Result.objects.all()
            result_queryset_serializer = ResultSerializer(result_queryset, many=True)
            return Response(result_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            bid = kwargs.get('bid')
            result_serializer = ResultSerializer(Result.objects.get(pk=bid))
            return Response(result_serializer.data, status=status.HTTP_200_OK)
