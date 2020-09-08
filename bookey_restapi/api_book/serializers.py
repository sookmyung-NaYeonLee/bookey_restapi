from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # 모델 Book의 모든 field를 serializer함.


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('bid', 'name', 'img_url')