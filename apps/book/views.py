from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.book.filter import BookFilter
from apps.book.models import Book
from apps.book.serializers import BookSerializers

class BookAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.ListModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              ):
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
