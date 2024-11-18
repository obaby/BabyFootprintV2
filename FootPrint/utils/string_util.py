# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/8/21 021 9:48
@Remark:
"""
import hashlib
import random
import re

CHAR_SET = ("2", "3", "4", "5",
            "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
            "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z")


def random_str(number=16):
    """
    返回特定长度的随机字符串(非进制)
    :return:
    """
    result = ""
    for i in range(0, number):
        inx = random.randint(0, len(CHAR_SET) - 1)
        result += CHAR_SET[inx]
    return result


def has_md5(str, salt='123456'):
    """
    md5 加密
    :param str:
    :param salt:
    :return:
    """
    # satl是盐值，默认是123456
    str = str + salt
    md = hashlib.md5()  # 构造一个md5对象
    md.update(str.encode())
    res = md.hexdigest()
    return res


def baby_validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == '__main__':
    # 测试邮箱验证函数
    emails = ['test1@example.com', 'invalid_email', '@example.com','notice@service.nai.dog','微信@wechat.com','zhongling@obaby.org.cn']
    for email in emails:
        print(f"{email}: {baby_validate_email(email)}")
