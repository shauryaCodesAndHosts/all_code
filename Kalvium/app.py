import os 
from flask import Flask
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_restful import Api, Resource
#from application.api import * 


app = None 
api = None

def createAppApi():
    print("**************************")
    app = Flask(__name__)
    print("**************************")
    app.config.from_object(LocalDevelopmentConfig)
    print("**************************")
    db.init_app(app)
    print("**************************")
    app.app_context().push()
    print("**************************")
    api = Api(app)
    print("**************************")
    return app , api 

app , api = createAppApi()


from application.controllers import *
#api.add_resource(Maths,'/<string:query>')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000' )