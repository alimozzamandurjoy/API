from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.models import Book
from .serializers import BookSerialzer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer