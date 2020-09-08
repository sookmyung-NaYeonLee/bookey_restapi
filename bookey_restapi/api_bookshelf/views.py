from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookshelfSerializer
from .serializers import BookshelfInfoSerializer
from rest_framework import status
from .models import Bookshelf



class BookshelfView(APIView):
    def post(self, request):
        bookshelf_serializer = BookshelfSerializer(data=request.data)

        if bookshelf_serializer.is_valid():
            bookshelf_serializer.save()
            return Response(bookshelf_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(bookshelf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('userId') is None and kwargs.get('bookId') is None:
            bookshelf_queryset = Bookshelf.objects.all()
            bookshelf_queryset_serializer = BookshelfSerializer(bookshelf_queryset, many=True)
            return Response(bookshelf_queryset_serializer.data, status=status.HTTP_200_OK)

        else:
            userId = kwargs.get('userId')
            bookId = kwargs.get('bookId')
            bookshelf_queryset = Bookshelf.objects.get(uid=userId, bid=bookId)

            bookshelf_queryset_serializer = BookshelfInfoSerializer(bookshelf_queryset)
            return Response(bookshelf_queryset_serializer.data, status=status.HTTP_200_OK)


    def put(self, request, **kwargs):
        if kwargs.get('userId') is None or kwargs.get('bookId') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

        else:
            userId = kwargs.get('userId')
            bookId = kwargs.get('bookId')
            bookshelf_object = Bookshelf.objects.get(uid=userId, bid=bookId)

            update_bookshelf_serializer = BookshelfSerializer(bookshelf_object, data=request.data)
            if update_bookshelf_serializer.is_valid():
                update_bookshelf_serializer.save()
                return Response(update_bookshelf_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('userId') is None or kwargs.get('bookId') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            userId = kwargs.get('userId')
            bookId = kwargs.get('bookId')
            bookshelf_object = Bookshelf.objects.filter(uid=userId, bid=bookId)
            bookshelf_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)

class BookshelfSearchView(APIView):
    def get(self, request, **kwargs):
        userId = kwargs.get('userId')
        bookshelf_queryset = Bookshelf.objects.filter(uid=userId)
        bookshelf_queryset_serializer = BookshelfInfoSerializer(bookshelf_queryset, many=True)
        return Response(bookshelf_queryset_serializer.data, status=status.HTTP_200_OK)
