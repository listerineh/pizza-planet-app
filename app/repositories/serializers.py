from app.plugins import ma
from .models import Ingredient, Size, Order, IngredientsDetail, BeveragesDetail, Beverage


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class IngredientsDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientsDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )


class BeveragesDetailSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeveragesDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )


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
