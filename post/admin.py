from django.contrib import admin
from post.models import Product, Category, Review

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)