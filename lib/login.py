# -*- coding:utf-8 -*-
import requests
from common.util.logger import console
from common.util.logger import logger
from lib.props.api import login_api
import simplejson
from common.util.Md5 import Md5


def login():
    user_name = '13600000002'
    password = Md5.md5('123456')
    post_data = {'requestPara': simplejson.dumps({'userName': user_name, 'password': password})}
    session_object = requests.session()
    object_cookie = session_object.post(url=login_api, data=post_data)
    console.debug(object_cookie.json())
    console.debug(type(object_cookie.json()))

    try:
        session_token = {"session_object": session_object,
                         "token": object_cookie.json()['data']['userInfo']['token']}
    except:
        logger.info("用户名或密码不对!")
        return 0
    return session_token
