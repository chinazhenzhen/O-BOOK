#flask核心对象
#业务逻辑写在模型层
from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure') #核心对象导入配置文件
    app.config.from_object('app.setting') #核心对象导入配置文件
    register_blueprint(app) #蓝图注册

    db.init_app(app)
    db.create_all(app=app)
    return app

#蓝图注册函数
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)