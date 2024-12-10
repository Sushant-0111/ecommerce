
from django.contrib import admin
from django.urls import path
from .views import CategoryViewSet
from .views import ProductViewSet
from rest_framework import routers


router = routers.SimpleRouter()


router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)

urlpatterns = []+router.urls
