from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'description', 'created_at')
    list_filter = ('id', 'title', 'category', 'description', 'created_at')
    search_fields = ('title', 'description')
    fields = ('title', 'category', 'description', 'created_at')
    readonly_fields = ('id', 'created_at')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'grade')
    list_filter = ('id', 'author', 'product', 'text', 'grade')
    search_fields = ('author', 'product', 'grade')
    fields = ('author', 'product', 'text', 'grade')
    readonly_fields = ('id', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
