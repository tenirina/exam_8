from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from webapp.models import Product, Review


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avm_grade'] = {}
        for i in range(len(context['products'])):
            context['avm_grade'][str(i + 1)] = 0
            num = 0
            for el in Review.objects.filter(product=context['products'][i]):
                context['avm_grade'][str(i + 1)] += el.grade
                num += 1
            if context['avm_grade'][str(i + 1)] != 0:
                context['avm_grade'][str(i + 1)] //= num
                context['avm_grade'][str(i + 1)] = [0] * context['avm_grade'][str(i + 1)]
        return context
