from django.contrib.auth import get_user_model
from django.db import models

from webapp.models import Product


class Review(models.Model):
    author = models.ForeignKey(to=get_user_model(), verbose_name='Author', related_name='reviews', null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, verbose_name='webapp.Product', related_name='reviews', null=False, blank=False, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text', max_length=200, null=False)
    grade = models.IntegerField(verbose_name='Grade', null=False)
    status = models.BooleanField(verbose_name='Status', default=False)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)


