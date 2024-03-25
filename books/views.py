from django.shortcuts import render
from books.models import Book
from django.views.generic import ListView
# Create your views here.
class BookListView(ListView):
    template_name = "book_list.html"
    model = Book