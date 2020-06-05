from MyApp import db, ma

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, nam, description, price, qty):
        self.name = nam
        self.description = description
        self.price = price
        self.qty = qty

# product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)