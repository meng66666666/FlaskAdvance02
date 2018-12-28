from flask_restful import Api

from MarshalApp.api.fruit import *
from MarshalApp.api.parse import StudentResource, CakeResource

api = Api()

def init_api(app):
    api.init_app(app)

#注册资源
api.add_resource(FruitResource,"/fruits/",)
api.add_resource(FruitSingleResource,"/fruit/<pk>/",)
api.add_resource(StudentResource,"/students/")
api.add_resource(CakeResource,"/cakes/")