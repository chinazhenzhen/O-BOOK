from flask import jsonify

from helper import is_isbn_or_key
from o_book import OBook


@app.route('/book/search/<q>/<page>') #尖括号被识别为参数
def search(q,page):
    '''

    :return:
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = OBook.search_by_isbn(q)
    else:
        result = OBook.search_by_keyword(q)
    return jsonify(result)  #利用flask函数返回json数据
