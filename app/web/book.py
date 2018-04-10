from flask import jsonify, request

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel
from app.libs.helper import is_isbn_or_key
from app.spider.o_book import OBook
from . import web


# 试图函数

@web.route('/book/search') #尖括号被识别为参数
def search():
    '''

    :return:
    '''
    #q = request.args['q']
    #至少有一个字符
    #page = request.args['page']
    #正整数

    #验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = OBook.search_by_isbn(q)
            result = BookViewModel.package_single(result,q)
        else:
            result = OBook.search_by_keyword(q,page)
            result = BookViewModel.package_collection(result,q)
        return jsonify(result)  #利用flask函数返回json数据
    else:
        return jsonify(form.errors)

@web.route('/test')
def test():
    return 'cccccc'
