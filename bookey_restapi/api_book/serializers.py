from rest_framework import serializers
from .models import Book, BestSeller


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # 모델 Book의 모든 field를 serializer함.


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('bid', 'title', 'img_url')


class BestSellerSerializer(serializers.ModelSerializer):
    bid = BookSerializer(read_only=True)
    class Meta:
        model = BestSeller
        fields = ('bid', 'rank')


class BestSellerRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSeller
        fields = ('rank')