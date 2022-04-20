from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import order.views
from . import views
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('news', views.NewsListView)
router.register('products', views.ProductsListView)
router.register('help', views.HelpListView)
router.register('slider', views.SliderListView)
router.register('color', views.ColorListView)
router.register('order', order.views.OrderListView)
router.register('cart', order.views.CartListView)
router.register('cartitem', order.views.CartItemListView)



urlpatterns = [
    path('aboutus/', views.AboutUsListView.as_view(), name="aboutus-list"),
    path('similar_product/<pk>/', similar_product),
    path('list_product/<pk>/', list_product),
    path('new_product/<pk>/', new_product),
    path('hit_of_sales/', hit_of_sales),
    path('new/', new),
    path('footer', footer),
    path('public_offer', public_offer),
    path('advantages/', advantages),
    path('favorite/', favorite),
    path('product_search', views.product_search),

    path('', include(router.urls))
]
