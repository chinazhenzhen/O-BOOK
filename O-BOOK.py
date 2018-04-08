
#web应用的主执行文件

from app import create_app

__author__ = 'chinazz'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])