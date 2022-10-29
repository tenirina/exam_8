from django.db import models
from django.db.models import TextChoices


class CategoriesChoices(TextChoices):
    FRUIT = 'FRUIT', 'Fruit'
    MEAT = 'MEAT', 'Meat'
    VEGETABLES = 'VEGETABLES', 'Vegetables'


class Product(models.Model):
    title = models.CharField(verbose_name='Title', null=False, blank=False, max_length=25)
    category = models.CharField(verbose_name='Category', choices=CategoriesChoices.choices, max_length=25, default=CategoriesChoices.VEGETABLES)
    description = models.TextField(verbose_name='Description', max_length=150)
    image = models.ImageField(verbose_name='Photo', null=True, blank=False, upload_to='product')
    is_deleted = models.BooleanField(verbose_name='Delete', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Deletion date', null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
