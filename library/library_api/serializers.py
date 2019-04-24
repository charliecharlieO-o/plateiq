from django.contrib.auth.models import User
from library_api.models import Author, Book, Stock
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'added_on', 'book_count')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'ISBN', 'added_on')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'book', 'ends_on', 'added_on')


class DeepBookSerializer(serializers.ModelSerializer):
    stock_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'ISBN', 'added_on', 'stock_count')
        depth = 1
