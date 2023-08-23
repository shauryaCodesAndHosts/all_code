from flask_restful import Resource,reqparse
from flask import request
from .models import *
from flask import jsonify

product_parser = reqparse.RequestParser()
product_parser.add_argument('productName', type=str, required=True)
product_parser.add_argument('expiryDate', type=str)
product_parser.add_argument('manufacturingDate', type=str)
product_parser.add_argument('ratePerUnit', type=float, required=True)
product_parser.add_argument('categoryId', type=int, required=True)
product_parser.add_argument('inStock', type=int, required=True)
product_parser.add_argument('timeOfEntry', type=str)

# Request parser for parsing JSON data
category_parser = reqparse.RequestParser()
category_parser.add_argument('categoryName', type=str, required=True)


class ManagerProductsResource(Resource):
    def post(self):
        data = request.json
        new_product = Product(
            productName=data['productName'],
            expiryDate=data['expiryDate'],
            manufacturingDate=data['manufacturingDate'],
            ratePerUnit=data['ratePerUnit'],
            categoryId=data['categoryId'],
            inStock=data['inStock'],
            timeOfEntry=data['timeOfEntry']
        )
        db.session.add(new_product)
        print(new_product)
        db.session.commit()
        return {'message': 'Product created successfully'}, 201

    def get(self):
        products = Product.query.all()
        print(products)
        ls=[]
        for product in products:
            ls.append(product.serialize())
        #print(ls)
        print(jsonify(ls))
        return ls, 200

class ManagerProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        if product:
            return product.serialize(), 200
        return {'message': 'Product not found'}, 404

    def put(self, product_id):
        product = Product.query.get(product_id)
        if product:
            data = request.json
            product.productName = data['productName']
            product.expiryDate = data['expiryDate']
            product.manufacturingDate = data['manufacturingDate']
            product.ratePerUnit = data['ratePerUnit']
            product.categoryId = data['categoryId']
            product.inStock = data['inStock']
            product.timeOfEntry = data['timeOfEntry']
            db.session.commit()
            return {'message': 'Product updated successfully'}, 200
        return {'message': 'Product not found'}, 404

    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted successfully'}, 200
        return {'message': 'Product not found'}, 404

class ManagerCategoriesResource(Resource):
    def post(self):
        data = request.json
        new_category = Category(categoryName=data['categoryName'])
        db.session.add(new_category)
        db.session.commit()
        return {'message': 'Category created successfully'}, 201

    def get(self):
        categories = Category.query.all()
        return jsonify([category.serialize() for category in categories]), 200

class ManagerCategoryResource(Resource):
    def get(self, category_id):
        category = Category.query.get(category_id)
        if category:
            return category.serialize(), 200
        return {'message': 'Category not found'}, 404

    def put(self, category_id):
        category = Category.query.get(category_id)
        if category:
            data = request.json
            category.categoryName = data['categoryName']
            db.session.commit()
            return {'message': 'Category updated successfully'}, 200
        return {'message': 'Category not found'}, 404

    def delete(self, category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return {'message': 'Category deleted successfully'}, 200
        return {'message': 'Category not found'}, 404

