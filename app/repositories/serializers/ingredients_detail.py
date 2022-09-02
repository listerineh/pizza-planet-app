from app.plugins import ma
from ..models import IngredientsDetail
from .ingredient import IngredientSerializer


class IngredientsDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientsDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )
