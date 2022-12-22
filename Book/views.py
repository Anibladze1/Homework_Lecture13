from django.shortcuts import render


def home(request):
    return render(request, 'Book/home.html')


def book_info(request):
    return render(request, 'Book/books.html')


