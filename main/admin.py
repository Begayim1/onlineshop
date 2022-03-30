from django.contrib import admin
from .models import *
# from main.models import Gallery, Product

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Image)

# class GalleryInline(admin.TabularInline):
#     fk_name = 'product'
#     model = Gallery
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [GalleryInline, ]
