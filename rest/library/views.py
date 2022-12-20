from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from library.serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer