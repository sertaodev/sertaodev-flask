from flask import Flask, request, jsonify
from .models import Products, db
from .serializer import ProdSchema


def init_app(app: Flask):

    @app.route('/', methods=['GET'])
    def index():
        return {"ola": "mundo"}

    @app.route('/prod', methods=['GET'])
    def list_prod():

        prod = ProdSchema(many=True)
        result = Products.query.all()
        return prod.jsonify(result), 200

    @app.route('/prod/add', methods=['POST'])
    def add_prod():
        prod = ProdSchema()
        data = prod.load(request.json, session=db.session)
        print(request.json['GTIN'])
        query = Products.query.filter(
            Products.GTIN == request.json['GTIN']).first()
        print(query)
        if(query == None):
            db.session.add(data)
            db.session.commit()
            return prod.jsonify(data), 201
        else:
            return jsonify({"Prod": "Already exists"}), 400

    @app.route('/prod/delete/<gtin>', methods=['DELETE'])
    def del_prod(gtin):
        data = Products.query.filter(Products.GTIN == gtin).delete()
        if(data == True):
            db.session.commit()
            return jsonify({"Delete Prod": gtin}), 201
        else:
            return jsonify({"Prod": "not found"}), 404

    @app.route('/prod/update/<gtin>', methods=['PUT'])
    def up_prod(gtin):
        prod = ProdSchema()
        data = Products.query.filter(Products.GTIN == gtin)
        if(data.first() != None):
            data.update(request.json)
            db.session.commit()
            return prod.jsonify(request.json), 201
        else:

            return jsonify({"Prod": "not found"}), 404
