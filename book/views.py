from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .serializers import BookSerializer
from book.forms import *
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_view(request):
    books = Book.objects.all()
    return render(request, 'testapp/book.html', {'books': books})

def book_input(request, id=None):
    book = get_object_or_404(Book, id=id) if id else None
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_view')
    return render(request, 'testapp/bookedit.html', {'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_view')