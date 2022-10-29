from django.views.generic import DetailView

from webapp.models import Product


class ProductsView(DetailView):
    template_name = 'products/product.html'
    model = Product
