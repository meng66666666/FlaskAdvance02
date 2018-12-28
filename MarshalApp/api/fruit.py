from flask import request
from flask_restful import Resource, fields, marshal_with, marshal, abort

from MarshalApp.models import Fruit, db

#创建水果对象的输出模板
fruit_fields = {
    "fruit_name":fields.String(attribute="name"),
    "price":fields.Float,
}

output_fields = {
    "status":fields.String,
    "msg":fields.String,
    "data":fields.Nested(fruit_fields),#嵌入
}
#fruit_fields对象，因为没有对象类型，所以Nested嵌入另一个字典对象fruit_fields

output_list_fields = {
    "status":fields.String,
    "msg":fields.String,
    "data":fields.List(fields.Nested(fruit_fields))
}
#再用output_list_fields方式实施
class FruitResource(Resource):
    @marshal_with(output_fields)
    def get(self):
        fruits = Fruit.query.all()
        data = {
            "status":"200",
            "msg":"ok",
            "data":fruits,
        }
        return data
    #也可以返回fruits对象为一个列表
    @marshal_with(output_fields)
    def post(self):
        fruit_name = request.form.get("name")
        fruit_price = request.form.get("price")
        new_fruit = Fruit(name=fruit_name,price=fruit_price)
        db.session.add(new_fruit)
        db.session.commit()
        data = {
            "status":"200",
            "msg":"ok",
            "data":new_fruit
        }
        return data

class FruitSingleResource(Resource):
    #主键pk或者_id
    # @marshal_with(fruit_fields)
    # def get(self,pk):
    #     fruit = Fruit.query.get(pk)
    #     return fruit
    def get(self, pk):
        fruit = Fruit.query.get(pk)
        #返回marshal函数也可以定制格式化输出
        if fruit is None:
            abort(404,message="请求的数据不存在！")
        return marshal(fruit,fruit_fields)