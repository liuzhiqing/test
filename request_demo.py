#!/usr//env python
#coding:utf8
import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>Response Headers:'
    print response.headers
    print '>>>Response Body:'
    print response.text

def use_params_requests():
    params = {'param1': 'hello','param2': 'world'}
    #发送请求
    response = requests.get(URL_IP,params=params)
    #处理响应
    print '>>>Response Headers:'
    print response.headers
    print '>>>Respons Status Code:'
    print response.status_code
    print response.reason
    print '>>>Response Body:'
    print response.json()

if __name__ == '__main__':
    print ">>>Use simple requests:"
    use_simple_requests()
    print ">>>Use params requests:"
    use_params_requests()
