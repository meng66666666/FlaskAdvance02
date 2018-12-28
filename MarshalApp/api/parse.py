from flask_restful import reqparse, Resource

#实例化RequestParser对象，“创建枪”
parser = reqparse.RequestParser()
#添加将要解析的参数，“装子弹”;required必须的;help提示;dest指定接收的参数名(用得少)
parser.add_argument("name",required=True,help="必须输入姓名!!!",dest="stuname")
parser.add_argument("age",type=int)
parser.add_argument("score",required=True,help="必须输入成绩!")
parser.add_argument("hobby",action="append")

parser2 = reqparse.RequestParser()
parser2.add_argument("cakename",location='form')#消息体中接收参数
parser2.add_argument("cakeprice",location='args')#url后面接收参数

parser2.add_argument("User-Agent",location="headers",dest='suv')

class StudentResource(Resource):

    def post(self):
        # 解析参数,“开枪”
        args = parser.parse_args()
        #通过dest关键字参数指定的别名获取参数
        stuname = args.get("stuname")
        stuage = args.get("age")
        stuscore = args.get("score")
        hobby = args.get("hobby")
        return {"stuname":stuname,"stuage":stuage,"stuscore":stuscore,"hobby":hobby}


class CakeResource(Resource):
    def post(self):
        args = parser2.parse_args()
        cakename = args.get('cakename')
        cakeprice = args.get('cakeprice')
        user_agent = args.get('suv')
        print("cakename=",cakename)
        print("cakeprice=",cakeprice)

        return {"cakename":cakename,"cakeprice":cakeprice,"user_agent":user_agent}










