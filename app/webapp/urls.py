from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductView, ProductUpdateView, ProductCreateView, ProductDeleteView
from webapp.views.reviews import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review_create', ReviewCreateView.as_view(), name='review_create'),
    path('product/<int:pk>/review_update', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:pk>/review_delete', ReviewDeleteView.as_view(), name='review_delete'),
]
