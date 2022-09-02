from datetime import date

from app.plugins import db


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.String(20), default=str(
        date.today().strftime("%d/%m/%Y")))
    total_price = db.Column(db.Float)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))

    size = db.relationship('Size', backref=db.backref('size'))
    ingredientsDetail = db.relationship(
        'IngredientsDetail', backref=db.backref('ingredients_detail'))
    beveragesDetail = db.relationship(
        'BeveragesDetail', backref=db.backref('beverages_detail'))
