
from .serializer import CategorySerializer
from .serializer import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .models import Product
from store.pagination import ProductPagination
from django_filters import rest_framework as filters
from store.filters import ProductFilterSet
from rest_framework.filters import SearchFilter 


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProductFilterSet
    search_fields = ["name",]