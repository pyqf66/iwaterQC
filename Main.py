# coding=utf-8
import requests
import simplejson
from lib.login import login
import pytest
from common.util.Md5 import Md5

pytest.main("-s -v ./test/test_queryUserAddressList.py --html=./logs/report.html")
# from common.util.logger import logger
# from common.util.logger import console
# from appium import webdriver
# import pytest
# import time
#
# # deviceName由adb devices获得
# config = dict()
# config['platformName'] = 'Android'
# config['platformVersion'] = '23'
# config['deviceName'] = '9013741d'
# config['appPackage'] = 'com.iwater'
# driver = webdriver.Remote('http://192.168.1.201:4723/wd/hub', config)
# time.sleep(3)
# # 滑动页面
# driver.swipe(800, 497, 30, 497, 1000)
# time.sleep(1)
# driver.swipe(800, 497, 30, 497, 1000)
# time.sleep(1)
# driver.swipe(800, 497, 30, 497, 1000)
# time.sleep(1)
# class Main(object):
#     try
#     return water:
#         tmp_var = 1 + "1"
#         logger.debug(tmp_var)
#     except:
#         logger.exception("捕获到错误")
# pytest.main("-s -v ./test/test_template.py --html=./logs/report.html")
#

# url = "http://127.0.0.1:8000/iwaterMock/v1/user/nt/login/v1.json"
# url = "http://123.57.47.236:8091/v1/user/nt/login/v1.json"
# url = "http://101.200.219.159:8081/iwaterMock/v1/user/nt/login/v1.json"
# url = "http://192.168.1.231:18088/iwaterMock/v1/user/nt/login/v1.json"
# password=Md5.md5("123456789")
# data = {'requestPara': simplejson.dumps({'userName': '13693019506', 'password': password})}
# data = {'requestPara': simplejson.dumps({'userName': '13693019506', 'password': password})}
# print(type(data))
# print(data)
# headers={'Content-type':"application/x-www-form-urlencode"}
# resp = requests.post(url=url,data=data ,headers=headers)
# resp = requests.post(url=url, data=data)
# content = resp.content
# print(resp.content.decode("utf-8"))
