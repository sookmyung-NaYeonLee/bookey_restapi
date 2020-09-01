from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import AppUser

class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request,  **kwargs):
        if kwargs.get('uid') is None:
            user_queryset = AppUser.objects.all()
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            user_serializer = UserSerializer(AppUser.objects.get(pk=uid))
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = AppUser.objects.get(pk=uid)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = AppUser.objects.get(pk=uid)
            user_object.delete()
            return Response("delete ok", status=status.HTTP_200_OK)