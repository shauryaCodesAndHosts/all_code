import os 
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig 
from application.database import db
from flask_bcrypt import Bcrypt
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint

app = None
api=None

def createApp():
    app=Flask(__name__,template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    api=Api(app)
    print(app)
    return app,api

app , api =createApp()

#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(current_dir,'calibrationOfTools.sqlite3')

bcrypt=Bcrypt(app)

#from application.controllers import *
#from application.managerControllers import * 
from application.customerControllers import *
from application.api import *

api.add_resource(ManagerProductsResource, '/api/manager/products')
api.add_resource(ManagerProductResource, '/api/manager/products/<int:product_id>')
api.add_resource(ManagerCategoriesResource, '/api/manager/categories')
api.add_resource(ManagerCategoryResource, '/api/manager/categories/<int:category_id>')

SWAGGER_URL = '/api/swagger'
API_URL = '/api/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')