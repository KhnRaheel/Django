from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Avg


# Create your views here.
from .models import Book
def index(request):
    books= Book.objects.all().order_by("-rating")
    num_books= books.count()
    avg=books.aggregate(Avg("rating"))

    return render(request, "book/index.html",{
        "books":books,
        "total_number_books":num_books,
        "average_rating":avg


    })

def book_detail(request, slug):
    book= get_object_or_404(Book, slug=slug)

    return render(request,"book/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling


    })