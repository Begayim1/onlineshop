from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Image)

admin.site.register(ImageUs)
admin.site.register(News)
admin.site.register(Advantages)
admin.site.register(Help)


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


class ListOfReferencesAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = Footer


@admin.register(PublicOffer)
class PublicOfferAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and PublicOffer.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = PublicOffer


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and Slider.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = Slider


class ImageUsForPhoto(admin.TabularInline):
    model = ImageUs
    max_num = 3


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and AboutUs.objects.exists():
            has_add = False
        return has_add

    list_display = ('id', 'name')

    inlines = [
        ImageUsForPhoto
    ]

    class Meta:
        model = AboutUs

@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and ImageHelp.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = ImageHelp

admin.site.register(ListOfReferences, ListOfReferencesAdmin)
admin.site.register(Product, ProductAdmin)
