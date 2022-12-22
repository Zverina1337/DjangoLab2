from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from library.serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework.permissions import IsAdminUser
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
class AuthorViewSetReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class BookViewSetReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__name', 'author__lastName', 'author__middle_name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAdminUser]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            if (Book.objects.get(title=request.data['title']).publisher != request.data['publisher'] and request.data[
                'genre'] == 'художественное произведение, переведенное с другого языка'):
                serializer.is_valid()
            if (Book.objects.get(title=request.data['title']).yearofRel != request.data['yearOfRel'] and request.data[
                'genre'] == 'учебник'):
                serializer.is_valid()
            else:
                raise ValidationError(self.errors)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes=[IsAdminUser]