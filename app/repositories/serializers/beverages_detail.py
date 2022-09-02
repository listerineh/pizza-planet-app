from app.plugins import ma
from ..models import BeveragesDetail
from .beverage import BeverageSerializer


class BeveragesDetailSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeveragesDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )
