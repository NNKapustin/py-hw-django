from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.db.models import Q

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('products')
        search_query = self.request.query_params.get('search')
        queryset = Stock.objects.all()
        if product_id:
            queryset = queryset.filter(positions__product_id=product_id)
        elif search_query:
            queryset = queryset.filter(
                Q(positions__product__title__icontains=search_query) | 
                Q(positions__product__description__icontains=search_query)
                )
        return queryset
    