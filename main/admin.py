from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(AboutUs)
admin.site.register(ImageUs)
admin.site.register(Collection)
admin.site.register(News)
admin.site.register(Advantages)
admin.site.register(PublicOffer)
admin.site.register(Help)
admin.site.register(ImageHelp)
admin.site.register(Slider)
admin.site.register(Footer)
admin.site.register(ReturnCall)
admin.site.register(ListOfReferences)


class ColorForPhoto(admin.TabularInline):
    model = Color
    max_num = 8


class ImageForPhoto(admin.TabularInline):
    model = Image
    max_num = 8


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')

    inlines = [
        ImageForPhoto,
        ColorForPhoto
    ]


admin.site.register(Product, ProductAdmin)
