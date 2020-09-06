from rest_framework import serializers
from .models import Bookshelf


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = '__all__'
        # 모델 User의 모든 field를 serializer함.