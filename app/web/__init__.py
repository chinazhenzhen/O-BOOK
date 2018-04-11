#web为python包，优先执行__init__文件
#蓝图注册
from flask import Blueprint

web = Blueprint('web',__package__)

#注册蓝图导入相关模块
from app.web import book,auth,drift,gift,main,wish