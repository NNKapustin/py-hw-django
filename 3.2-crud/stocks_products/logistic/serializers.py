from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = 'product', 'quantity', 'price'


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = 'address', 'positions'
    
    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)
        for position in positions:
            product = position.pop('product')
            StockProduct.objects.create(stock=stock, product=product, **position)
        return stock
    
    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        for position in positions:
            product = position.pop('product')
            stock_product, _ = StockProduct.objects.get_or_create(stock=instance, product=product)
            stock_product.quantity = position.get('quantity', stock_product.quantity)
            stock_product.price = position.get('price', stock_product.price)
            stock_product.save()
        return instance




