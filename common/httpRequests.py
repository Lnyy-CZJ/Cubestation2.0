#封装定义框架专属的http请求能力
import time

import requests


class httpRequests(object):

    def __init__(self, url):
        self.url = url
        self.req = requests.session()
        self.time = int(time.time() * 1000)
        # 自定义请求头，根据自身所在公司项目需求
        self.headers = {'Content-Type': 'application/json', 'clientEventTime': self.time,'appId': 2}

    # 封装get请求
    def get(self, url='', params='', data='', headers=None, token=None):
        response = self.req.get(url=url, params=params, data=data, headers=headers, token=token)
        return response

    # post请求
    def post(self, url='', params='', data='', headers=None, token=None):
        response = self.req.post(url=url, params=params, data=data, headers=headers, token=token)
        return response

    # put请求
    def put(self, url='', params='', data='', headers=None, token=None):
        response = self.req.put(url=url, params=params, data=data, headers=headers, token=token)
        return response

    # delete请求
    def delete(self, url='', params='', data='', headers=None, token=None):
        response = self.req.delete(url=url, params=params, data=data, headers=headers, token=token)
        return response