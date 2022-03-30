from django.contrib import admin
from django.urls import path, include
from . import views
from .views import SimilarProductsView

urlpatterns = [
    path('', views.ProductListView.as_view(), name = "products-list"),

]