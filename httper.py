import requests

class HTTP:
    #静态方法装饰器，没有用到类中的变量
    @staticmethod
    def get(url,return_json=True):
        r= requests.get(url)
        #restful 返会json

        #三联表达式简化if else
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text