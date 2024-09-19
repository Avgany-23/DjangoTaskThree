from django.urls import path
import phones.views


urlpatterns = [
    path('', phones.views.index),
    path('catalog/', phones.views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', phones.views.show_product, name='phone'),
]


