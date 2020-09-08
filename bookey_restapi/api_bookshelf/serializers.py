from rest_framework import serializers
from .models import Bookshelf
from api_book.serializers import *

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = '__all__'
        # 모델 Bookshelf의 모든 field를 serializer함.


class BookshelfInfoSerializer(serializers.ModelSerializer):
    class Meta:
        bookinfo = BookInfoSerializer(read_only=True)
        class Meta:
            model = Bookshelf
            fields = ('bookinfo', 'review')
