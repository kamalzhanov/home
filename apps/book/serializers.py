from rest_framework import serializers

from apps.book.models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'