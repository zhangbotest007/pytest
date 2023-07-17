"""
====================
@Time:  2023/7/1214:21
@Author: test_007
@File:  handle_parameterize.py
====================
"""
import re
import string
import random
import csv

class Parameterize:
    """
    参数化类
    """
    ont_existed_user_pattern = r'{ont_existed_user}'
    ont_existed_tel_pattern = r'{ont_existed_tel}'

    @staticmethod
    def creat_user():
        """
        随机生成用户
        """
        return ''.join(random.choices(string.ascii_letters, k=9))

    @staticmethod
    def creat_tel():
        """
        随机生成手机号
        """
        return '130' + ''.join(random.sample('012345679', 8))

    @classmethod
    def to_param(cls, data):
        data1 = str(data)
        if re.search(cls.ont_existed_user_pattern, data1):

            data = re.sub(cls.ont_existed_user_pattern, cls.creat_user(), data1)

        if re.search(cls.ont_existed_tel_pattern, data1):
            data = re.sub(cls.ont_existed_tel_pattern, cls.creat_tel(), data1)

        return data


if __name__ == '__main__':
    res = Parameterize()
    # # res1 = res.creat_user()
    # # print(res1, type(res1))
    # # res2 = res.creat_tel()
    # # print(res2, type(res2))
    res1 = res.to_param('{ont_existed_user}')
    print(res1)

