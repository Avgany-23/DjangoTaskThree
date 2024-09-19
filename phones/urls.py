from django.urls import path
from .views import ShowProduct, ShowCatalog, Index


urlpatterns = [
    path('', Index.as_view()),
    path('catalog/', ShowCatalog.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', ShowProduct.as_view(), name='phone'),
]
