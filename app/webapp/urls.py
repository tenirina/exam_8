from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductsView.as_view(), name='product'),
]
