from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductView, ProductUpdateView, ProductCreateView, ProductDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
