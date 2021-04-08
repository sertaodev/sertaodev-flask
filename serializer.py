from flask import Flask
from flask_marshmallow import Marshmallow

from .models import Products

ma = Marshmallow()


def configure(app: Flask):
    ma.init_app(app)


class ProdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        include_fk = True
        load_instance = True
