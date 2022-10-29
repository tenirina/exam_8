from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product, Review


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avm_grade'] = 0
        num = 0
        for el in Review.objects.filter(product=self.object):
            context['avm_grade'] += el.grade
            num += 1
        if context['avm_grade'] != 0:
            context['avm_grade'] //= num
        context['avm_grade'] = [0] * context['avm_grade']
        return context


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_product'
    template_name = 'products/update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
            kwargs['files'] = self.request.FILES
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse("product", kwargs={'pk': self.object.pk})


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.create_product'
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_product'
    template_name = 'products/confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
