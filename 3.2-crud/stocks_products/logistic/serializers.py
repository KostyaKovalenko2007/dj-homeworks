from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id','title','description']

    pass


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model  =  StockProduct
        fields = [
            'id',
            'product',
            'quantity',
            'price'
        ]
    pass


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = [ 'id',
                   'address',
                  'positions'
                  ]

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for position in positions:
            StockProduct.objects.create(stock = stock,**position)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        ##Тупо не для данной бизнеслогики подойдет
        # update_or_create() как я понимаю не удаляет объекты если
        #StockProduct.objects.filter(stock=stock).delete()

        for position in positions:
            obj, created = StockProduct.objects.update_or_create(
                                                            id=StockProduct\
                                                                .objects\
                                                                .filter(stock=stock)\
                                                                .filter(product=position.get("product"))\
                                                                .get(),
                                                            **position
                                                            )
        return stock
