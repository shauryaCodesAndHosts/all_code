from flask_restful import Resource
from flask import request
from .models import *
from flask import jsonify

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
        print(new_product.productName)
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
            print(product.serialize())
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
        return ([category.serialize() for category in categories]), 200

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

class ManagerCategoriesProductResource(Resource):
    def get(self, categoryId, productId):
        category = Category.query.filter_by(categoryId=categoryId).first()
        product = Product.query.filter_by(categoryId = category.categoryId, productId= productId ).first()
        return product.serialize() , 200
        return '' , 404