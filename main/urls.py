from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('collection', views.CollectionListView)
router.register('news', views.NewsListView)
router.register('products',views.ProductsListView)
router.register('public', views.PublicOfferListView)
router.register('slider', views.SliderListView)


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
    path('collection/', collection),
    path('advantages/', advantages),
    # path('similar_products/<int:pk>/', SimilarListView.as_view(), name="similar-list"),

    # path('news/', views.NewsListView.as_view(), name="news-list"),
    # path('', views.CollectionListView.as_view(), name="collections-list")
    path('', include(router.urls))
]

