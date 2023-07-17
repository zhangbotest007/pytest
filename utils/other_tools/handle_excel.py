"""
====================
@Time:  2023/7/516:24
@Author: test_007
@File:  handle_excel.py
====================
"""
import os
import openpyxl
# from utils.other_tools.handle_yaml import get_yaml
from utils.other_tools.handle_path import CONFIG_FILES
from utils.other_tools.handle_path import CONFIG_TEST_CASE_PARAMETER


class CaseDate:
    pass


class HandleExcel(object):
    """封装excel读写的类"""

    def __init__(self, sheet_name, filename=None):
        self.sheet_name = sheet_name
        if filename is not None:
            self.filename = os.path.join(CONFIG_TEST_CASE_PARAMETER, filename)
        # else:
            # self.filename = os.path.join(CONFIG_TEST_CASE_PARAMETER, get_yaml.yaml_read('case_common', 'excel_file_name'))

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_excel_obj(self):
        self.open()
        case_datas = []
        rows = list(self.sh.rows)
        datas_title = ['data', 'assert_data']
        titles = [title_datas.value for title_datas in rows[0]]
        for datas in rows[1:]:
            cases_data_list = []
            keyword = titles.index('status_code')
            data_title = titles[1:keyword]
            status_code = titles[keyword]
            all_param_data = [data.value for data in datas]
            if all_param_data[0] is None:
                break
            case_data_list = [data for data in all_param_data[1:keyword]]
            case_data_dict = dict(zip(data_title, case_data_list))
            cases_data_list.append(case_data_dict)
            case_assert_dict = {}
            case_assert_dict[status_code] = all_param_data[keyword]
            while keyword + 1 < len(datas):
                data_ele = all_param_data[keyword + 1]
                if data_ele is None:
                    break
                else:
                    assert_data = titles[keyword + 2:keyword + 6]
                    datas_data = all_param_data[keyword + 2:keyword + 6]
                    datas_data[2] = str(datas_data[2])
                    assert_datas = dict(zip(assert_data, datas_data))
                    case_assert_dict[data_ele] = assert_datas
                    keyword += 5
            cases_data_list.append(case_assert_dict)
            case_data_object = CaseDate()
            for data_object in zip(datas_title, cases_data_list):
                setattr(case_data_object, data_object[0], data_object[1])
            case_datas.append(case_data_object)
        return case_datas


if __name__ == '__main__':
    excel = HandleExcel('login_02', 'login.xlsx')
    res = excel.read_excel_obj()
    print(res)
    for i in res:
        print(i.data)
        print(i.assert_data)
