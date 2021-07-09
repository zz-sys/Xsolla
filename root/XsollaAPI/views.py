from XsollaAPI.serializers import *
from XsollaAPI.paginations import *
from XsollaAPI.models import *
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


# ViewSet for Product
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = StandartSetPagination

    def get_queryset(self):
        if self.request.query_params.get('limit') is None:
            return Product.objects.all()
        else:
            if int(self.request.query_params.get('limit')) > 100:
                raise ValidationError({'error': 'limit is greater than 100'}, code=400)
            else:
                return Product.objects.all()


# ViewSet for StockUnit
class StockUnitViewSet(viewsets.ModelViewSet):
    serializer_class = StockUnitSerializer
    pagination_class = StandartSetPagination

    def get_queryset(self):
        if self.request.query_params.get('limit') is None:
            return StockUnit.objects.all()
        else:
            if int(self.request.query_params.get('limit')) > 100:
                raise ValidationError({'error': 'limit is greater than 100'}, code=400)
            else:
                return StockUnit.objects.all()

    def create(self, request, *args, **kwargs):
        product_data = request.data
        new_stockunit = StockUnit.objects.create(product_type=Product.objects.get(id=product_data['product_type'])
                                                 , sku=product_data['sku'], description=product_data['description'])
        new_stockunit.save()
        serializer = StockUnitSerializer(new_stockunit)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        stockunit = self.get_object()
        data = request.data
        product = Product.objects.get(id=data['product_type'])
        stockunit.product_type = product
        stockunit.sku = data['sku']
        stockunit.description = data['description']
        stockunit.save()

        serializer = StockUnitSerializer(stockunit)
        return Response(serializer.data)


# viewSet for UnitAtStorage
class UnitAtStorageViewSet(viewsets.ModelViewSet):
    serializer_class = UnitAtStorageSerializer
    pagination_class = StandartSetPagination

    def get_queryset(self):

        if self.request.query_params.get('limit') is None:
            return UnitAtStorage.objects.all()
        else:
            if int(self.request.query_params.get('limit')) > 100:
                raise ValidationError({'error': 'limit is greater than 100'}, code=400)
            else:
                return UnitAtStorage.objects.all()

    def create(self, request, *args, **kwargs):
        uas_data = request.data

        new_unitas = UnitAtStorage.objects.create(sku=StockUnit.objects.get(sku=uas_data['sku']),
                                                  count=uas_data['count'],
                                                  cost=uas_data['cost'])
        new_unitas.save()
        serializer = UnitAtStorageSerializer(new_unitas)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        uas = self.get_object()
        uas_data = request.data

        uas.sku = StockUnit.objects.get(sku=uas_data['sku'])
        uas.count = uas_data['count']
        uas.cost = uas_data['cost']

        uas.save()
        serializer = UnitAtStorageSerializer(uas)
        return Response(serializer.data)
