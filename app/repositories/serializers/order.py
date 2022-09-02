from app.plugins import ma
from ..models import Order
from .size import SizeSerializer
from .ingredients_detail import IngredientsDetailSerializer
from .beverages_detail import BeveragesDetailSerializer


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredientsDetail = ma.Nested(IngredientsDetailSerializer, many=True)
    beveragesDetail = ma.Nested(BeveragesDetailSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'ingredientsDetail',
            'beveragesDetail'
        )
