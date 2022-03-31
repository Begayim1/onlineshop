from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.ProductListView.as_view(), name="products-list"),
    path('', views.AboutUsListView.as_view(), name="about_us-list"),

]