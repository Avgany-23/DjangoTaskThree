from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F


class BooksView(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail_book.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = kwargs['object'].pub_date
        prev_date = Book.objects.filter(pub_date__lt=current_date).order_by('-pub_date').first()
        next_date = Book.objects.filter(pub_date__gt=current_date).order_by('pub_date').first()
        if prev_date:
            prev_date = prev_date.pub_date.year
        else:
            prev_date = None
        if next_date:
            next_date = next_date.pub_date.year
        else:
            next_date = None
        return {**context, 'prev_date': prev_date, 'next_date': next_date}


class BooksListDate(ListView):
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        print(self.kwargs, 99999)
        books = Book.objects.filter(pub_date__year=self.kwargs['date'])
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = self.kwargs['date']
        prev_date = Book.objects.filter(pub_date__year__lt=current_date).order_by('-pub_date').first()
        next_date = Book.objects.filter(pub_date__year__gt=current_date).order_by('pub_date').first()
        if prev_date:
            prev_date = prev_date.pub_date.year
        else:
            prev_date = None
        if next_date:
            next_date = next_date.pub_date.year
        else:
            next_date = None
        return {**context, 'prev_date': prev_date, 'next_date': next_date, 'current_date': current_date}
