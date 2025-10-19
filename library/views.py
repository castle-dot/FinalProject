from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, LibraryUser
from .serializers import BookSerializer, LibraryUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all().order_by('title')
    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()
        if book.copies_available > 0:
            book.copies_available -= 1
            book.save()
            return Response({'status': f'{book.title} checked out successfully!'})
        else:
            return Response({'error': 'No copies available'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        book = self.get_object()
        book.copies_available += 1
        book.save()
        return Response({'status': f'{book.title} returned successfully!'})


class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    def get_queryset(self):
        return LibraryUser.objects.all().order_by('username')