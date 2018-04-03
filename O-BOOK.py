from flask import Flask


__author__ = 'chinazz'

app = Flask(__name__)
app.config.from_object('config')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])