from flask import jsonify, request,render_template,flash
import json

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        O_Book = OBook()

        if isbn_or_key == 'isbn':
            O_Book.search_by_isbn(q)
        else:
            O_Book.search_by_keyword(q,page)

        books.fill(O_Book,q)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")

    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    o_book = OBook()
    o_book.search_by_isbn(isbn)
    book = BookViewModel(o_book.first)
    return render_template('book_detail.html',book=book,wishes=[],gifts=[])

@web.route('/test')
def test():
    return 'cccccc'
