from django.views.generic import ListView, RedirectView, DetailView
from phones.models import Phone


class Index(RedirectView):
    url = 'catalog'


class ShowCatalog(ListView):
    template_name = 'phones/catalog.html'
    queryset = Phone.objects.all()
    context_object_name = 'phones'

    def get_ordering(self):
        sort = self.request.GET.get('sort')
        if sort == 'name':
            return ['-name']
        if sort == 'min_price':
            return ['price']
        if sort == 'max_price':
            return ['-price']


class ShowProduct(DetailView):
    model = Phone
    template_name = 'phones/product.html'
