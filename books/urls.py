from django.urls import path
from .views import BooksView, BookDetail, BooksListDate

urlpatterns = [
    path('', BooksView.as_view()),
    path('date/<str:date>', BooksListDate.as_view(), name='list_date_books'),
    path('<int:pk>', BookDetail.as_view(), name='book_detail'),
]
