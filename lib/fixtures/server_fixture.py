# -*- coding:utf-8 -*-
import pytest
from lib.login import login


@pytest.fixture()
def server_fixture():
    return login()
