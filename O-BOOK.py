'''
#web应用的主执行文件

from app import create_app

__author__ = 'chinazz'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],threaded=True)
'''

from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # 如果要使用vscode调试，需要将debug设置为False，否则无法命中请求断点
    app.run(debug=True)
