from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status
from .models import Book


class BookView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('bid') is None:
            book_queryset = Book.objects.all()  # 모든 User의 정보를 불러온다.
            book_queryset_serializer = BookSerializer(book_queryset, many=True)
            return Response(book_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            bid = kwargs.get('bid')
            book_serializer = BookSerializer(Book.objects.get(pk=bid))
            return Response(book_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)  # Request의 data를 BookSerializer로 변환

        if book_serializer.is_valid():
            book_serializer.save()  # BookSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달
        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        if kwargs.get('bid') is None:
            Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            bid = kwargs.get('bid')
            book_object = Book.objects.get(pk=bid)

            update_book_serializer = BookSerializer(book_object, data=request.data)
            if update_book_serializer.is_valid():
                update_book_serializer.save()
                return Response(update_book_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('bid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            bid = kwargs.get('bid')
            book_object = Book.objects.get(pk=bid)
            book_object.delete()
            return Response("book delete ok", status=status.HTTP_200_OK)