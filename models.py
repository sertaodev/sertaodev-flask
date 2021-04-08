from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app: Flask):
    db.init_app(app)
    app.db = db


class Products(db.Model):
    GTIN = db.Column(db.String(120), unique=True,
                     nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.String(120),  nullable=False)
    price = db.Column(db.Float,  nullable=False)
    supplier = db.Column(db.String(120),  nullable=False)
