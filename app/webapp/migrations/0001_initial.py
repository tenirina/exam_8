# Generated by Django 4.1.2 on 2022-10-29 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Title')),
                ('category', models.CharField(choices=[('FRUIT', 'Fruit'), ('MEAT', 'Meat'), ('VEGETABLES', 'Vegetables')], default='VEGETABLES', max_length=25, verbose_name='Category')),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='product', verbose_name='Photo')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Deletion date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='Text')),
                ('grade', models.IntegerField(verbose_name='Grade')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='webapp.product', verbose_name='webapp.Product')),
            ],
        ),
    ]