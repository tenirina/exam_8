from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/create.html'
    form_class = ReviewForm
    model = Review

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            grade = form.cleaned_data.get('grade')
            user = request.user
            Review.objects.create(author=user, product=product, text=text, grade=grade)
        return redirect('product', pk=product.pk)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'reviews/update.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    success_url = reverse_lazy('index')


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'reviews/confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')
