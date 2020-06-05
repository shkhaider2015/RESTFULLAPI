from flask import Blueprint, jsonify, request
from MyApp.models import Product, product_schema
from MyApp import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get():
    return jsonify({ 'name' : 'haidetr' })

@main.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)