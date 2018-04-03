from flask import Flask

__author__ = 'chinazz'

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>') #尖括号被识别为参数
def search(q,page):
    '''

    :return:
    '''
    #ISBN13 ISBN10
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'