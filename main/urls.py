from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('collection', views.CollectionListView)
router.register('news',views.NewsListView)

urlpatterns = [
    path('product/', views.ProductListView.as_view(), name="products-list"),
    path('about/', views.AboutUsListView.as_view(), name="about_us-list"),
    # path('news/', views.NewsListView.as_view(), name="news-list"),
    # path('', views.CollectionListView.as_view(), name="collections-list")
    path('',include(router.urls))
]

