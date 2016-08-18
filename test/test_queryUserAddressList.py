# -*- coding:utf-8 -*-
from lib.fixtures.server_fixture import server_fixture
from lib.props.api import queryUserAddressList_api
from lib.cases.case_queryUserAddressList import *
import simplejson
import pytest


@pytest.mark.parametrize("input_data,expected", [(1, case1), (2, case2)])
def test_queryUserAddressList_with_cookie(server_fixture, input_data, expected):
    session_object = server_fixture["session_object"]
    token = server_fixture["token"]
    data = {'requestPara': simplejson.dumps({'token': token})}
    resp = session_object.post(url=queryUserAddressList_api, data=data)
    assert resp.json() == expected
