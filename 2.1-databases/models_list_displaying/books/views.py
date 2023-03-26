from django.shortcuts import render
from .models import Book
from datetime import date


def books_view(request):
    template = 'books/books_list.html'

    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def books_view_by_Date(request, dt):
    template = 'books/books_list_by_date.html'
    nxt = Book.objects.filter(pub_date__gt=dt).order_by('pub_date').first()
    prv = Book.objects.filter(pub_date__lt=dt).order_by('pub_date').first()

    context = {
        'books': Book.objects.filter(pub_date=dt),
        'pagi_next': nxt.pub_date.strftime("%Y-%m-%d") if nxt is not None else None,
        'pagi_prev': prv.pub_date.strftime("%Y-%m-%d") if prv is not None else None,
    }
    return render(request, template, context)
