#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2023-07-13 10:20:52

import copy
import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['login_01', 'login_02']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("中台接口测试案例")
@allure.feature("登录模块")
class TestLogin:

    @allure.story("登录功能测试")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_login(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        try:
            in_data['assert_data']['status_code'] is True
        except KeyError as e:
            for i, j in in_data['assert_data'].items():
                data = copy.deepcopy(in_data)
                case_datas = data['data'][i]
                case_assert = j
                data['assert_data'] = case_assert
                data['data'] = case_datas
                res = RequestControl(data).http_request()
                TearDownHandler(res).teardown_handle()
                Assert(assert_data=data['assert_data'],
                       sql_data=res.sql_data,
                       request_data=res.body,
                       response_data=res.response_data,
                       status_code=res.status_code).assert_type_handle()
        else:
            res = RequestControl(in_data).http_request()
            TearDownHandler(res).teardown_handle()
            Assert(assert_data=in_data['assert_data'],
                   sql_data=res.sql_data,
                   request_data=res.body,
                   response_data=res.response_data,
                   status_code=res.status_code).assert_type_handle()


if __name__ == '__main__':
    pytest.main(['test_test_login.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
