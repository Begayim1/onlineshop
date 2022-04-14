from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import order.views
from . import views
from rest_framework.routers import DefaultRouter

from .views import *
from order.views import *



router = DefaultRouter()
router.register('collection', views.CollectionListView)
router.register('news', views.NewsListView)
router.register('products',views.ProductsListView)
router.register('public', views.PublicOfferListView)
router.register('slider', views.SliderListView)
router.register('site', views.ReturnCallListView)
router.register('order', order.views.OrderListView)
router.register('cart', order.views.CartListView)
router.register('cart/item', order.views.CartItemListView)





urlpatterns = [
    path('product/', views.ProductListView.as_view(), name="products-list"),
    path('about/', views.AboutUsListView.as_view(), name="about_us-list"),
    path('help/', views.HelpListView.as_view(), name="help-list"),
    path('similar_product/<pk>/', similar_product),
    path('list_product/<pk>/', list_product),
    path('new_product/<pk>/', new_product),
    path('footer/', footer),
    path('hit_of_sales/', hit_of_sales),
    path('new/', new),
    path('collections/<id>', collection),
    path('advantages/', advantages),
    path('favorite/', favorite),


    path('', include(router.urls))
]

