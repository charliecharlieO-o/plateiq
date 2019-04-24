from library_api.models import Author, Book, Stock
from rest_framework import viewsets
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from library_api.serializers import (
    AuthorSerializer, BookSerializer, StockSerializer,
    DeepBookSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.annotate(
        book_count=Count('book')
    ).all().order_by('-added_on')
    serializer_class = AuthorSerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        authors = Author.objects.all().order_by('-added_on')
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.annotate(
        stock_count=Count('stock')
    ).all().order_by('-added_on')
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DeepBookSerializer
        else:
            return BookSerializer

    @action(detail=False, methods=['post'])
    def search(self, request):
        query = request.data['query']
        queryset = Book.objects.annotate(
            stock_count=Count('stock')
        ).filter(title__search=query).order_by('-added_on')
        serializer = DeepBookSerializer(queryset, many=True)
        return Response(serializer.data)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('-added_on')
    serializer_class = StockSerializer
