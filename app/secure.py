# 机密信息配置信息 secure

DEBUG = True
SECRET_KEY = 'CHINAZZ'
#sqlalchemy 支持分布式数据库链接
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/OBook'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Email 配置
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'hello@yushu.im'
MAIL_PASSWORD = 'Bmwzy1314520'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'


# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5


WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = True

from datetime import timedelta
REMEMBER_COOKIE_DURATION = timedelta(days=30)

PROXY_API = 'http://ip.yushu.im/get'
